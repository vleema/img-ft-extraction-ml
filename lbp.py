import argparse
import os

from os import listdir
from os.path import isfile, join

import numpy as np
import pandas as pd

from skimage.color import rgb2gray
from skimage.feature import local_binary_pattern
from skimage.io import imread
from skimage.transform import resize

from common import iscat, isdog


def main():
    parser = argparse.ArgumentParser()
    _ = parser.add_argument(
        "-r",
        "--resolucao",
        help="resolucao da imagem",
        default=256,
        type=int,
    )
    _ = parser.add_argument(
        "-R",
        "--raio",
        help="raio do lbp",
        default=3,
        type=int,
    )
    _ = parser.add_argument(
        "-d",
        "--dataset-path",
        help="caminho das imagens",
        default="./images",
        type=str,
    )
    args = parser.parse_args()

    res = args.resolucao
    radius = args.raio
    path = args.dataset_path

    files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    print(f"extraindo features, com parâmetros: resolução={res}, raio={radius}...")
    data = extract_features(files, res, radius)

    try:
        os.mkdir("out")
    except FileExistsError:
        pass
    os.chdir("./out")

    cat = np.asarray(data["cat_feats"])
    dog = np.asarray(data["dog_feats"])

    xs = np.vstack([cat, dog])
    ys = np.array(["cat"] * len(cat) + ["dog"] * len(dog))

    result = pd.DataFrame(xs, columns=[f"feat_{i + 1}" for i in range(xs.shape[1])])
    result["label"] = ys

    lbp_out = f"LBP_{res}_{radius}R.csv"
    result.to_csv(lbp_out, index=False)

    print(f"arquivo lbp={lbp_out} escrito")


def extract_features(
    files: list[str],
    res: int,
    radius: int,
) -> dict[str, list[float]]:
    points = radius * 2
    cat_feats = []
    dog_feats = []

    for file in files:
        img = resize(imread(file), (res, res), anti_aliasing=True)
        grayed_img = (rgb2gray(img) * 255).astype(np.uint8)

        lbp = local_binary_pattern(grayed_img, points, radius, method="uniform")
        hist, _ = np.histogram(lbp.ravel(), bins=points + 2, range=(0, points + 2))
        hist = hist.astype(np.float64)
        hist /= hist.sum()

        if iscat(file):
            cat_feats.append(hist)
        elif isdog(file):
            dog_feats.append(hist)

    return {"cat_feats": cat_feats, "dog_feats": dog_feats}


if __name__ == "__main__":
    main()

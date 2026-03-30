import argparse
import os

from os import listdir
from os.path import isfile, join
from typing import Any

import pandas as pd
import numpy as np

from skimage.io import imread
from skimage.color import rgb2gray
from skimage.feature import hog
from skimage.transform import resize
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from common import iscat, isdog


def main():
    parser = argparse.ArgumentParser()
    _ = parser.add_argument(
        "-r",
        "--resolucao",
        help="resolução do bloco do hog",
        default=256,
        type=int,
    )
    _ = parser.add_argument(
        "-p",
        "--pixels",
        help="pixels por célula",
        default=32,
        type=int,
    )
    _ = parser.add_argument(
        "-d",
        "--dataset-path",
        help="caminho das imagens",
        default="./images",
        type=str,
    )
    _ = parser.add_argument(
        "-P",
        "--pca",
        help="porcentagem de componentes no PCA",
        default=0.9,
        type=float,
    )
    args = parser.parse_args()

    res = args.resolucao
    px = args.pixels
    path = args.dataset_path
    components = args.pca

    files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

    print(
        f"extraindo features, com parâmetros: resolução={res}, pixels={px}, componentes={components}..."
    )
    data = extract_features(files, res, px)

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

    print(f"executando pca com componentes={components}...")
    pca = exec_pca(result, components)

    hog_out = f"HOG_{res}_{px}x{px}.csv"
    result.to_csv(hog_out, index=False)

    pca_out = f"PCA_0{f'{components:.2f}'.split('.')[1]}_{hog_out}"
    pca.to_csv(pca_out, index=False)

    print(f"arquivos, hog={hog_out}, pca={pca_out} escritos")


def extract_features(
    files: list[str],
    res: int,
    pixels: int,
) -> dict[str, list[float]]:
    cat_feats = []
    dog_feats = []
    for file in files:
        img = resize(imread(file), (res, res), anti_aliasing=True)
        grayed_img = rgb2gray(img)
        feat = hog(
            grayed_img,
            pixels_per_cell=(pixels, pixels),
        )
        if iscat(file):
            cat_feats.append(feat)
        elif isdog(file):
            dog_feats.append(feat)

    return {"cat_feats": cat_feats, "dog_feats": dog_feats}


def exec_pca(df: pd.DataFrame, n_components: float) -> pd.DataFrame:
    xs = df.drop(columns="label")
    ys = df["label"]

    std = StandardScaler().fit_transform(xs)
    pca = PCA(n_components=n_components, whiten=True).fit_transform(std)

    ret = pd.DataFrame(data=pca, columns=[f"feat_{i}" for i in range(pca.shape[1])])
    ret["label"] = ys.values

    return ret


if __name__ == "__main__":
    main()

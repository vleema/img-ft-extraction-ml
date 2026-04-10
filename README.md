# Notebooks para extração de características de imagens e algoritmos de classificação

> **Autores:** Vinicius de Lima e Alexandre Maciel

As bases são geradas pelo notebook [bases.ipynb](./bases.ipynb) e ficam no
diretório `./out` relativo a execução do notebook. Os datasets gerados foram os
seguintes:

**HOG:**

| Resolução | Píxels por célula | Atributos | Bases             |
| --------- | ----------------- | --------- | ----------------- |
| 256x256   | 32x32             | 2.916     | HOG_256_32x32.csv |
| 256x256   | 16x16             | 15.876    | HOG_256_16x16.csv |
| 256x256   | 8x8               | 72.900    | HOG_256_8x8.csv   |
| 128x128   | 32x32             | 324       | HOG_128_32x32.csv |
| 128x128   | 16x16             | 2.916     | HOG_128_16x16.csv |
| 128x128   | 8x8               | 15.876    | HOG_128_8x8.csv   |

**PCA**

| Método  | HOG               | Atributos | Bases                     |
| ------- | ----------------- | --------- | ------------------------- |
| PCA 90% | HOG_128_32x32.csv | 61        | PCA_090_HOG_128_32x32.csv |
| PCA 90% | HOG_128_16x16.csv | 214       | PCA_090_HOG_128_16x16.csv |
| PCA 90% | HOG_128_8x8.csv   | 479       | PCA_090_HOG_128_8x8.csv   |
| PCA 75% | HOG_128_32x32.csv | 29        | PCA_075_HOG_128_32x32.csv |
| PCA 75% | HOG_128_16x16.csv | 106       | PCA_075_HOG_128_16x16.csv |
| PCA 75% | HOG_128_8x8.csv   | 280       | PCA_075_HOG_128_8x8.csv   |
| PCA 90% | HOG_256_32x32.csv | 177       | PCA_090_HOG_256_32x32.csv |
| PCA 90% | HOG_256_16x16.csv | 429       | PCA_090_HOG_256_16x16.csv |
| PCA 90% | HOG_256_8x8.csv   | 599       | PCA_090_HOG_256_8x8.csv   |
| PCA 75% | HOG_256_32x32.csv | 83        | PCA_075_HOG_256_32x32.csv |
| PCA 75% | HOG_256_16x16.csv | 236       | PCA_075_HOG_256_16x16.csv |
| PCA 75% | HOG_256_8x8.csv   | 399       | PCA_075_HOG_256_8x8.csv   |

**LBP**

| Resolução | Raio | Atributos | Bases           |
| --------- | ---- | --------- | --------------- |
| 256x256   | 12   | 26        | LBP_256_12R.csv |
| 256x256   | 6    | 14        | LBP_256_6R.csv  |
| 256x256   | 3    | 8         | LBP_256_3R.csv  |

## Recursos

- Link do dataset: <https://www.robots.ox.ac.uk/~vgg/data/pets/>
- Link das bases processadas:
  <https://drive.proton.me/urls/F1QHRERWRC#gCiIxFLpfla3>

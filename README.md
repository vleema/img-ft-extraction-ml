# Projeto 01 - Extração de características baseadas em HOG e LBP

**Autores:** Vinicius de Lima e Alexandre Maciel

O gerenciamento de dependências é feito com o [uv](https://docs.astral.sh/uv/)
com versão do python sendo a 3.14. A sincronia de dependências é realizada com:

```bash
uv sync
```

E a execução de um script é realizado através de:

```bash
uv run <nome_do_script>
```

Para extrair as características das imagens, foram definidos dois scripts,
`hog.py` e `lbp.py`. Um que executa o método de extração de características
[HOG](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_hog.html)
e outro o
[LBP](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_local_binary_pattern.html).
Ambos os scripts leem as imagens que tem os nomes `Russian_Blue`, `Birman`,
`samoyed` e `pug` de um diretório chamando `images`, extraem suas características em features e colocam o resultado num csv seguinte formato:

```csv
feat_1,feat_2,feat_3,...,feat_n,label
...
```

`label` pode ser `cat` ou `dog`, mas seu valor não é deduzido após a extração, e sim pelo nome da raça manualmente.

Ambos os scripts definem uma interface para a passagem de argumentos para as
extrações, isto é:

**lbp.py**

```terminal
$ uv run lbp.py -h
usage: lbp.py [-h] [-r RESOLUCAO] [-R RAIO] [-a ATRIBUTOS] [-d DATASET_PATH]

options:
  -h, --help                      show this help message and exit
  -r, --resolucao RESOLUCAO       resolucao da imagem
  -R, --raio RAIO                 raio do lbp
  -d, --dataset-path DATASET_PATH caminho das imagens
```

**hog.py**

```terminal
$ uv run hog.py -h
usage: hog.py [-h] [-r RESOLUCAO] [-p PIXELS] [-d DATASET_PATH] [-P PCA]

options:
  -h, --help                      show this help message and exit
  -r, --resolucao RESOLUCAO       resolução do bloco do hog
  -p, --pixels PIXELS             pixels por célula
  -d, --dataset-path DATASET_PATH caminho das imagens
  -P, --pca PCA                   porcentagem de componentes no PCA
```

Para gerar as bases descritas na especificação do projeto, foi implementado um
runner em shell (`run.sh`) que executa cada script de extração com os parâmetros descritos mais a frente:

```terminal
$ ./run.sh
...
RUN: executando lbp...
extraindo features, com parâmetros: resolução=256, raio=3, atributos=26...
arquivo lbp=LBP_256_3R_26A.csv escrito
extraindo features, com parâmetros: resolução=256, raio=6, atributos=50...
arquivo lbp=LBP_256_6R_50A.csv escrito
extraindo features, com parâmetros: resolução=256, raio=12, atributos=96...
arquivo lbp=LBP_256_12R_96A.csv escrito
```

As bases geradas ficam por padrão no diretório `./out` relativo a execução do
programa. As bases geradas foram as seguintes:

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

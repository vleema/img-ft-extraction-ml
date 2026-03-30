#!/usr/bin/env bash

# hog
RESOLUCOES=("256" "128")
PIXELS=("32" "16" "8")
COMPONENTES=("0.75" "0.90")

echo "RUN: executando hog..."
for cp in "${COMPONENTES[@]}"; do
    for res in "${RESOLUCOES[@]}"; do
        for px in "${PIXELS[@]}"; do
            uv run hog.py --resolucao "$res" --pixels "$px" --pca "$cp"
        done
    done
done

# lbp
RAIOS=("3" "6" "12")

echo "RUN: executando lbp..."
for r in "${RAIOS[@]}"; do
    uv run lbp.py --raio "$r"
done

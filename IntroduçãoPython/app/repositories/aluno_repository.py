import json
import os

CAMINHO = "data/alunos.json"


def carregar_dados():
    if not os.path.exists(CAMINHO):
        return {}

    with open(CAMINHO, "r") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(CAMINHO, "w") as f:
        json.dump(dados, f, indent=4)

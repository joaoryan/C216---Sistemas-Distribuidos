import json
import os

PASTA_DADOS = "data"
CAMINHO = os.path.join(PASTA_DADOS, "alunos.json")

ESTRUTURA_INICIAL = {
    "contadores": {"GES": 0, "GEC": 0},
    "alunos": {}
}

def inicializar_banco():
    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)
        
    if not os.path.exists(CAMINHO):
        with open(CAMINHO, "w") as f:
            json.dump(ESTRUTURA_INICIAL, f, indent=4)

def carregar_banco():
    inicializar_banco()
    with open(CAMINHO, "r") as f:
        return json.load(f)

def salvar_banco(dados):
    inicializar_banco()
    with open(CAMINHO, "w") as f:
        json.dump(dados, f, indent=4)


def carregar_dados():
    banco = carregar_banco()
    return banco["alunos"]

def salvar_dados(alunos_dados):
    banco = carregar_banco()
    banco["alunos"] = alunos_dados
    salvar_banco(banco)

def gerar_matricula(curso: str) -> int:
    banco = carregar_banco()
    curso = curso.upper()
    
    if curso not in banco["contadores"]:
        banco["contadores"][curso] = 0
        
    banco["contadores"][curso] += 1
    
    salvar_banco(banco)
    
    return banco["contadores"][curso]

def resetar_banco():
    salvar_banco(ESTRUTURA_INICIAL)
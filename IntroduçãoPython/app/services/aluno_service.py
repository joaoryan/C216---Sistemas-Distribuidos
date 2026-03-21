from app.models.aluno import Aluno
from app.repositories.aluno_repository import carregar_dados, salvar_dados
from app.utils.matricula import gerar_matricula

def criar_aluno(nome, email, curso):
    dados = carregar_dados()

    matricula = gerar_matricula(curso)
    aluno = Aluno(nome, email, curso, matricula)

    dados[matricula] = aluno.to_dict()
    salvar_dados(dados)

    return matricula


def listar_alunos():
    return carregar_dados()


def atualizar_aluno(matricula, nome, email):
    dados = carregar_dados()

    if matricula not in dados:
        return False

    dados[matricula]["nome"] = nome
    dados[matricula]["email"] = email

    salvar_dados(dados)
    return True


def remover_aluno(matricula):
    dados = carregar_dados()

    if matricula in dados:
        del dados[matricula]
        salvar_dados(dados)
        return True

    return False

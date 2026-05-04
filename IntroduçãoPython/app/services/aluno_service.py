from app.models.aluno import Aluno
from app.repositories.aluno_repository import carregar_dados, salvar_dados, gerar_matricula, resetar_banco

def criar_aluno(nome: str, email: str, curso: str):
    dados = carregar_dados()
    matricula = gerar_matricula(curso)
    
    aluno = Aluno(nome, email, curso, matricula)
    dados[aluno.id] = aluno.to_dict()
    
    salvar_dados(dados)
    return aluno.to_dict()

def listar_alunos():
    return list(carregar_dados().values())

def buscar_aluno_por_id(aluno_id: str):
    dados = carregar_dados()
    return dados.get(aluno_id)

def atualizar_aluno(aluno_id: str, dados_atualizados: dict):
    dados = carregar_dados()
    if aluno_id not in dados:
        return None

    for key, value in dados_atualizados.items():
        if value is not None:
            dados[aluno_id][key] = value

    salvar_dados(dados)
    return dados[aluno_id]

def remover_aluno(aluno_id: str):
    dados = carregar_dados()
    if aluno_id in dados:
        del dados[aluno_id]
        salvar_dados(dados)
        return True
    return False

def resetar_alunos():
    resetar_banco()
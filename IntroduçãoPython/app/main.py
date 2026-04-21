from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.aluno_service import (
    criar_aluno,
    listar_alunos,
    atualizar_aluno,
    remover_aluno
)

app = FastAPI(title="Sistema de Alunos")

class AlunoCreate(BaseModel):
    nome: str
    email: str
    curso: str

class AlunoUpdate(BaseModel):
    nome: str
    email: str

@app.post("/alunos/", status_code=201)
def cadastrar_aluno(aluno: AlunoCreate):
    matricula = criar_aluno(aluno.nome, aluno.email, aluno.curso)
    return {"mensagem": "Aluno cadastrado com sucesso", "matricula": matricula}

@app.get("/alunos/", status_code=200)
def obter_alunos():
    alunos = listar_alunos()
    return alunos

@app.put("/alunos/{matricula}", status_code=200)
def editar_aluno(matricula: str, aluno: AlunoUpdate):
    sucesso = atualizar_aluno(matricula, aluno.nome, aluno.email)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"mensagem": "Dados atualizados com sucesso"}

@app.delete("/alunos/{matricula}", status_code=200)
def deletar_aluno(matricula: str):
    sucesso = remover_aluno(matricula)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"mensagem": "Aluno removido com sucesso"}
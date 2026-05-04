from fastapi import FastAPI, HTTPException, APIRouter
from app.models.aluno import AlunoCreate, AlunoUpdate
from app.services import aluno_service

app = FastAPI(title="Gerenciador de Alunos")

router = APIRouter(prefix="/api/v1/alunos", tags=["Alunos"])

@router.post("/", status_code=201)
def cadastrar_aluno(aluno: AlunoCreate):
    if aluno.curso.upper() not in ["GES", "GEC"]:
        raise HTTPException(status_code=400, detail="Curso deve ser GES ou GEC")
        
    novo_aluno = aluno_service.criar_aluno(aluno.nome, aluno.email, aluno.curso)
    return novo_aluno

@router.get("/", status_code=200)
def obter_alunos():
    return aluno_service.listar_alunos()

@router.get("/{aluno_id}", status_code=200)
def obter_aluno_por_id(aluno_id: str):
    aluno = aluno_service.buscar_aluno_por_id(aluno_id.upper())
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.patch("/{aluno_id}", status_code=200)
def editar_aluno(aluno_id: str, aluno: AlunoUpdate):
    aluno_atualizado = aluno_service.atualizar_aluno(aluno_id.upper(), aluno.dict(exclude_unset=True))
    if not aluno_atualizado:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno_atualizado

@router.delete("/{aluno_id}", status_code=200)
def deletar_aluno(aluno_id: str):
    sucesso = aluno_service.remover_aluno(aluno_id.upper())
    if not sucesso:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"mensagem": "Aluno removido com sucesso"}

@router.delete("/", status_code=200)
def resetar_lista():
    aluno_service.resetar_alunos()
    return {"mensagem": "Lista de alunos resetada com sucesso"}

app.include_router(router)
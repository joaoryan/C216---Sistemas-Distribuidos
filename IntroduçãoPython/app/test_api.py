from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

matricula_teste = None

def test_criar_aluno():
    global matricula_teste
    response = client.post("/alunos/", json={
        "nome": "João", 
        "email": "joao@teste.com", 
        "curso": "GES"
    })
    assert response.status_code == 201
    dados = response.json()
    assert "matricula" in dados
    matricula_teste = dados["matricula"]

def test_listar_alunos():
    response = client.get("/alunos/")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_atualizar_aluno():
    global matricula_teste
    response = client.put(f"/alunos/{matricula_teste}", json={
        "nome": "João editado",
        "email": "joao.edit@teste.com"
    })
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Dados atualizados com sucesso"}

def test_remover_aluno():
    global matricula_teste
    response = client.delete(f"/alunos/{matricula_teste}")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Aluno removido com sucesso"}
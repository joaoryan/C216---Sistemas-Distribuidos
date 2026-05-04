from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def setup_function():
    client.delete("/api/v1/alunos/")

def test_crud_completo_alunos():
    for i in range(3):
        res = client.post("/api/v1/alunos/", json={"nome": f"Aluno GES {i}", "email": f"ges{i}@inatel.br", "curso": "GES"})
        assert res.status_code == 201

    for i in range(3):
        res = client.post("/api/v1/alunos/", json={"nome": f"Aluno GEC {i}", "email": f"gec{i}@inatel.br", "curso": "GEC"})
        assert res.status_code == 201

    res_listar = client.get("/api/v1/alunos/")
    assert res_listar.status_code == 200
    alunos = res_listar.json()
    assert len(alunos) == 6

    res_busca = client.get("/api/v1/alunos/GEC1")
    assert res_busca.status_code == 200
    assert res_busca.json()["nome"] == "Aluno GEC 0"

    res_patch = client.patch("/api/v1/alunos/GES2", json={"nome": "Nome Atualizado GES2"})
    assert res_patch.status_code == 200
    assert res_patch.json()["nome"] == "Nome Atualizado GES2"

    res_delete = client.delete("/api/v1/alunos/GEC2")
    assert res_delete.status_code == 200

    res_busca_removido = client.get("/api/v1/alunos/GEC2")
    assert res_busca_removido.status_code == 404

    res_novo_gec = client.post("/api/v1/alunos/", json={"nome": "Novo Aluno", "email": "novo@inatel.br", "curso": "GEC"})
    assert res_novo_gec.json()["id"] == "GEC4"
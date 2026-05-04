from pydantic import BaseModel
from typing import Optional

class Aluno:
    def __init__(self, nome: str, email: str, curso: str, matricula: int):
        self.nome = nome
        self.email = email
        self.curso = curso.upper()
        self.matricula = matricula
        self.id = f"{self.curso}{self.matricula}"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "curso": self.curso,
            "matricula": self.matricula
        }

class AlunoCreate(BaseModel):
    nome: str
    email: str
    curso: str

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    curso: Optional[str] = None
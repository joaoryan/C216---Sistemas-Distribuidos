class Aluno:
    def __init__(self, nome, email, curso, matricula):
        self.nome = nome
        self.email = email
        self.curso = curso
        self.matricula = matricula

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "curso": self.curso,
            "matricula": self.matricula
        }

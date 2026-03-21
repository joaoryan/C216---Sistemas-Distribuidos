from app.services.aluno_service import (
    criar_aluno,
    listar_alunos,
    atualizar_aluno,
    remover_aluno
)


def menu():
    while True:
        print("\n========== SISTEMA DE ALUNOS ==========")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Atualizar aluno")
        print("4 - Remover aluno")
        print("0 - Sair")
        print("======================================")

        op = input("Escolha uma opção: ")

        if op == "1":
            print("\n--- Cadastro de Aluno ---")
            nome = input("Nome: ")
            email = input("Email: ")
            curso = input("Curso (ex: GES, GEC): ").upper()

            matricula = criar_aluno(nome, email, curso)

            print("\n Aluno cadastrado com sucesso!")
            print(f" Matrícula gerada: {matricula}")

        elif op == "2":
            print("\n--- Lista de Alunos ---")
            alunos = listar_alunos()

            if not alunos:
                print(" Nenhum aluno cadastrado.")
            else:
                for m, d in alunos.items():
                    print("\n----------------------------------")
                    print(f"Matrícula: {m}")
                    print(f"Nome: {d['nome']}")
                    print(f"Email: {d['email']}")
                    print(f"Curso: {d['curso']}")
                print("\n----------------------------------")

        elif op == "3":
            print("\n--- Atualização de Aluno ---")
            m = input("Matrícula do aluno: ")
            nome = input("Novo nome: ")
            email = input("Novo email: ")

            if atualizar_aluno(m, nome, email):
                print("\n Dados atualizados com sucesso!")
            else:
                print("\n Aluno não encontrado.")

        elif op == "4":
            print("\n--- Remoção de Aluno ---")
            m = input("Matrícula do aluno: ")

            if remover_aluno(m):
                print("\n Aluno removido com sucesso.")
            else:
                print("\n Aluno não encontrado.")

        elif op == "0":
            print("\n Encerrando o sistema...")
            break

        else:
            print("\n Opção inválida. Tente novamente.")

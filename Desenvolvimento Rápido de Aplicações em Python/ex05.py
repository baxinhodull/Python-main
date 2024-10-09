import json
import os

# Nome do arquivo para armazenar os dados dos alunos
nome_arquivo = "alunos.json"

# Função para cadastrar um novo aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    curso = input("Digite o curso do aluno: ")
    
    aluno = {
        "nome": nome,
        "email": email,
        "curso": curso
    }
    
    # Verifica se o arquivo já existe e carrega os dados existentes
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            alunos = json.load(arquivo)
    else:
        alunos = []
    
    # Adiciona o novo aluno à lista
    alunos.append(aluno)
    
    # Salva os dados de volta no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(alunos, arquivo, indent=4)
    
    print(f"Aluno {nome} cadastrado com sucesso!")

# Função para listar todos os alunos cadastrados
def listar_alunos():
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            alunos = json.load(arquivo)
            if alunos:
                print("\nAlunos cadastrados:")
                for aluno in alunos:
                    print(f"Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}")
            else:
                print("Nenhum aluno cadastrado.")
    else:
        print("Nenhum aluno cadastrado.")

# Função para buscar um aluno pelo nome
def buscar_aluno():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")
    
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            alunos = json.load(arquivo)
            encontrado = False
            for aluno in alunos:
                if aluno['nome'].lower() == nome_busca.lower():
                    print(f"\nAluno encontrado: Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Aluno não encontrado.")
    else:
        print("Nenhum aluno cadastrado.")

# Função principal do menu
def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar um novo aluno")
        print("2. Listar alunos cadastrados")
        print("3. Buscar um aluno pelo nome")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_aluno()
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()

import json
import os
import tkinter as tk
from tkinter import messagebox

# Nome do arquivo para armazenar os dados dos alunos
nome_arquivo = "alunos.json"

# Função para salvar alunos no arquivo
def salvar_alunos(alunos):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(alunos, arquivo, indent=4)

# Função para carregar alunos do arquivo
def carregar_alunos():
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    return []

# Função para cadastrar um novo aluno
def cadastrar_aluno():
    nome = entry_nome.get()
    email = entry_email.get()
    curso = entry_curso.get()
    
    if not nome or not email or not curso:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")
        return
    
    aluno = {
        "nome": nome,
        "email": email,
        "curso": curso
    }
    
    alunos = carregar_alunos()
    alunos.append(aluno)
    salvar_alunos(alunos)
    
    messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso!")
    
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_curso.delete(0, tk.END)

# Função para listar todos os alunos cadastrados
def listar_alunos():
    alunos = carregar_alunos()
    if alunos:
        lista_alunos = "\n".join(f"Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}" for aluno in alunos)
        messagebox.showinfo("Alunos cadastrados", lista_alunos)
    else:
        messagebox.showinfo("Alunos cadastrados", "Nenhum aluno cadastrado.")

# Função para buscar um aluno pelo nome
def buscar_aluno():
    nome_busca = entry_busca.get()
    
    alunos = carregar_alunos()
    encontrado = False
    for aluno in alunos:
        if aluno['nome'].lower() == nome_busca.lower():
            messagebox.showinfo("Aluno encontrado", f"Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}")
            encontrado = True
            break
    if not encontrado:
        messagebox.showwarning("Atenção", "Aluno não encontrado.")

# Criação da janela principal
root = tk.Tk()
root.title("Gerenciador de Alunos")

# Campos para cadastro
tk.Label(root, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="E-mail:").grid(row=1, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Curso:").grid(row=2, column=0)
entry_curso = tk.Entry(root)
entry_curso.grid(row=2, column=1)

tk.Button(root, text="Cadastrar Aluno", command=cadastrar_aluno).grid(row=3, columnspan=2)

# Campos para busca
tk.Label(root, text="Buscar Aluno por Nome:").grid(row=4, column=0)
entry_busca = tk.Entry(root)
entry_busca.grid(row=4, column=1)

tk.Button(root, text="Buscar", command=buscar_aluno).grid(row=5, columnspan=2)

# Botão para listar alunos
tk.Button(root, text="Listar Alunos", command=listar_alunos).grid(row=6, columnspan=2)

# Iniciar o loop principal da interface
root.mainloop()

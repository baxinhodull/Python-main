import tkinter as tk
from tkinter import messagebox, ttk
import database

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento")
        self.login_frame()

    def login_frame(self):
        self.clear_frame()
        tk.Label(self.root, text="Usuário").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Button(self.root, text="Login", command=self.main_frame).pack()

    def main_frame(self):
        self.clear_frame()
        tk.Button(self.root, text="Cadastrar Cliente", command=self.cadastrar_cliente).pack()
        tk.Button(self.root, text="Listar Clientes", command=self.listar_clientes).pack()
        tk.Button(self.root, text="Sair", command=self.root.quit).pack()

    def cadastrar_cliente(self):
        self.clear_frame()
        tk.Label(self.root, text="Nome").pack()
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack()
        tk.Label(self.root, text="Email").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()
        tk.Label(self.root, text="Telefone").pack()
        self.telefone_entry = tk.Entry(self.root)
        self.telefone_entry.pack()
        tk.Label(self.root, text="Endereço").pack()
        self.endereco_entry = tk.Entry(self.root)
        self.endereco_entry.pack()
        tk.Button(self.root, text="Salvar", command=self.salvar_cliente).pack()

    def salvar_cliente(self):
        database.adicionar_cliente(
            self.nome_entry.get(),
            self.email_entry.get(),
            self.telefone_entry.get(),
            self.endereco_entry.get()
        )
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        self.main_frame()

    def listar_clientes(self):
        self.clear_frame()
        clientes = database.listar_clientes()
        for cliente in clientes:
            tk.Label(self.root, text=f"{cliente[1]} - {cliente[2]}").pack()
        tk.Button(self.root, text="Voltar", command=self.main_frame).pack()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    database.criar_tabela()
    root = tk.Tk()
    app = App(root)
    root.mainloop()

import sqlite3

def conectar():
    return sqlite3.connect('meu_banco.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(open("create_database.sql").read())
    conn.commit()
    conn.close()

def adicionar_cliente(nome, email, telefone, endereco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)",
                   (nome, email, telefone, endereco))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    return cursor.fetchall()

def atualizar_cliente(id, nome, email, telefone, endereco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nome=?, email=?, telefone=?, endereco=? WHERE id=?",
                   (nome, email, telefone, endereco, id))
    conn.commit()
    conn.close()

def remover_cliente(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
    conn.commit()
    conn.close()

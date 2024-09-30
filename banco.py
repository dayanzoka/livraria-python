import sqlite3
from pathlib import Path

BASE_DIR = Path("meu_sistema_livraria")
DATA_DIR = BASE_DIR / "data"
DB_FILE = DATA_DIR / "livraria.db"

DATA_DIR.mkdir(parents=True, exist_ok=True)

def conectar():
    return sqlite3.connect(DB_FILE)

def criar_tabela():
    conexao = conectar()
    query = '''CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                autor TEXT,
                ano_publicacao INTEGER,
                preco REAL)'''
    conexao.execute(query)
    conexao.commit()
    conexao.close()

def adicionar_livro(titulo, autor, ano_publicacao, preco):
    conexao = conectar()
    query = "INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)"
    conexao.execute(query, (titulo, autor, ano_publicacao, preco))
    conexao.commit()
    conexao.close()

def exibir_livros():
    conexao = conectar()
    query = "SELECT * FROM livros"
    livros = conexao.execute(query).fetchall()
    conexao.close()
    return livros

def atualizar_preco(id_livro, novo_preco):
    conexao = conectar()
    query = "UPDATE livros SET preco = ? WHERE id = ?"
    conexao.execute(query, (novo_preco, id_livro))
    conexao.commit()
    conexao.close()

def remover_livro(id_livro):
    conexao = conectar()
    query = "DELETE FROM livros WHERE id = ?"
    conexao.execute(query, (id_livro,))
    conexao.commit()
    conexao.close()

def buscar_por_autor(autor):
    conexao = conectar()
    query = "SELECT * FROM livros WHERE autor = ?"
    livros = conexao.execute(query, (autor,)).fetchall()
    conexao.close()
    return livros

import sqlite3
from pathlib import Path

# Diretório e arquivo do banco de dados
BASE_DIR = Path("meu_sistema_livraria")
DATA_DIR = BASE_DIR / "data"
DB_FILE = DATA_DIR / "livraria.db"

class BancoDeDados:
    def __init__(self):
        # Criar o diretório 'data' se ele não existir
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        # Conectar ao banco de dados
        self.conexao = sqlite3.connect(DB_FILE)
        self.criar_tabela()

    def criar_tabela(self):
        query = '''CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    autor TEXT,
                    ano_publicacao INTEGER,
                    preco REAL)'''
        self.conexao.execute(query)
        self.conexao.commit()

    def adicionar_livro(self, titulo, autor, ano_publicacao, preco):
        query = "INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)"
        self.conexao.execute(query, (titulo, autor, ano_publicacao, preco))
        self.conexao.commit()

    def exibir_livros(self):
        query = "SELECT * FROM livros"
        return self.conexao.execute(query).fetchall()

    def atualizar_preco(self, id_livro, novo_preco):
        query = "UPDATE livros SET preco = ? WHERE id = ?"
        self.conexao.execute(query, (novo_preco, id_livro))
        self.conexao.commit()

    def remover_livro(self, id_livro):
        query = "DELETE FROM livros WHERE id = ?"
        self.conexao.execute(query, (id_livro,))
        self.conexao.commit()

    def buscar_por_autor(self, autor):
        query = "SELECT * FROM livros WHERE autor = ?"
        return self.conexao.execute(query, (autor,)).fetchall()

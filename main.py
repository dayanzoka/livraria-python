import os
import shutil
import csv
from pathlib import Path
from datetime import datetime
from banco import criar_tabela, adicionar_livro, exibir_livros, atualizar_preco, remover_livro, buscar_por_autor

BASE_DIR = Path("meu_sistema_livraria")
BACKUP_DIR = BASE_DIR / "backups"
EXPORT_DIR = BASE_DIR / "exports"
DB_FILE = Path("meu_sistema_livraria/data/livraria.db")

os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)

db = BancoDeDados()  

def fazer_backup():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = BACKUP_DIR / f"backup_livraria_{timestamp}.db"
    shutil.copy(DB_FILE, backup_file)
    print(f"Backup realizado em: {backup_file}")

def exportar_para_csv():
    livros = db.exibir_livros()
    if livros:
        csv_file = EXPORT_DIR / "livros_exportados.csv"
        with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Título", "Autor", "Ano de Publicação", "Preço"])
            writer.writerows(livros)
        print(f"Dados exportados para {csv_file}")
    else:
        print("Nenhum livro para exportar.")

def importar_de_csv(csv_file_path):
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        livros = [(row["Título"], row["Autor"], row["Ano de Publicação"], row["Preço"]) for row in reader]
    for livro in livros:
        db.adicionar_livro(livro[0], livro[1], int(livro[2]), float(livro[3]))
    fazer_backup()

def adicionar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano_publicacao = int(input("Ano de Publicação: "))
    preco = float(input("Preço: "))
    db.adicionar_livro(titulo, autor, ano_publicacao, preco)
    fazer_backup()

def exibir_livros():
    livros = db.exibir_livros()
    if livros:
        for livro in livros:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Preço: {livro[4]}")
    else:
        print("Nenhum livro cadastrado.")

def atualizar_preco():
    id_livro = int(input("ID do Livro: "))
    novo_preco = float(input("Novo Preço: "))
    db.atualizar_preco(id_livro, novo_preco)
    fazer_backup()

def remover_livro():
    id_livro = int(input("ID do Livro a ser removido: "))
    db.remover_livro(id_livro)
    fazer_backup()

def buscar_por_autor():
    autor = input("Autor: ")
    livros = db.buscar_por_autor(autor)
    if livros:
        for livro in livros:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Preço: {livro[4]}")
    else:
        print(f"Nenhum livro encontrado para o autor {autor}.")

def menu():
    while True:
        print("\n----- Menu -----")
        print("1. Adicionar novo livro")
        print("2. Exibir todos os livros")
        print("3. Atualizar preço de um livro")
        print("4. Remover um livro")
        print("5. Buscar livros por autor")
        print("6. Exportar dados para CSV")
        print("7. Importar dados de CSV")
        print("8. Fazer backup do banco de dados")
        print("9. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_livro()
        elif escolha == '2':
            exibir_livros()
        elif escolha == '3':
            atualizar_preco()
        elif escolha == '4':
            remover_livro()
        elif escolha == '5':
            buscar_por_autor()
        elif escolha == '6':
            exportar_para_csv()
        elif escolha == '7':
            csv_path = input("Caminho do arquivo CSV: ")
            importar_de_csv(csv_path)
        elif escolha == '8':
            fazer_backup()
        elif escolha == '9':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

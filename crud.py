from database import db

def CREATE_livro():
    print("Jorge")

def READ_livros():
    conexao = db()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM livros")

    livros = cursor.fetchall()                 #pega todos os valores puxados pelo SELECT * FROM livros e armazena na variável livros

    conexao.close()

    return [dict(livros for livro in livros)]  #transforma os dados da variavel livros em um dictionary
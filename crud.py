from database import db
from models import Livro
import sqlite3

def CREATE_livro(titulo, autor, genero, paginas, status, data_inicio):
    conexao = db()
    cursor = conexao.cursor()

    cursor.execute("""INSERT INTO livros( 
                   titulo,
                   autor,
                   genero,
                   paginas,
                   status,
                   data_inicio) VALUES (?, ?, ?, ?, ?, ?)""", (titulo, autor, genero, paginas, status, data_inicio))
    
    conexao.commit()
    conexao.close()

def READ_livro():
    conexao = db()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM livros")

    livros = cursor.fetchall()                 #pega todos os valores puxados pelo SELECT * FROM livros e armazena na variável livros

    conexao.close()

    return [dict(livro) for livro in livros]  #transforma os dados da variavel livros em um dictionary

def EDIT_livro(ColunaQueVouEditar: str, Edicao: str):
    conexao = db()
    cursor = conexao.cursor()

    cursor.execute()

    conexao.commit()
    conexao.close()
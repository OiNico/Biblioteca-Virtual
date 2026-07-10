from fastapi import FastAPI
from crud import READ_livro, CREATE_livro, EDIT_livro
from models import Livro


app = FastAPI()

@app.get("/livros")
def Read_livros():
    return READ_livro()

@app.post("/livros")
def Create_livro():
    CREATE_livro(
        "Cartas de Um Diabo a Seu Aprendiz",
        "C.S. Lewis",
        "Literatura Fantástica",
        208,
        "Lendo",
        "10/07/2026"
    )
    return "Livro Criado com sucesso"

@app.put("/livros")
def Edit_livro():
    EDIT_livro()
    return "Livro editado com sucesso"
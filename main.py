from fastapi import FastAPI
from crud import READ_livros

app = FastAPI()

@app.get("/livros")
def Read_livros():
    return READ_livros()
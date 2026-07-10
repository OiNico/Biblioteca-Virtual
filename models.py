from pydantic import BaseModel

class Livro(BaseModel):
    titulo: str
    autor: str
    genero: str
    paginas: int
    status: str
    data_inicio: str
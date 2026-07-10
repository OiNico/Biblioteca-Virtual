import sqlite3

conexao = sqlite3.connect("database.db")
sqlite = conexao.cursor()

def db():
    conexao = sqlite3.connect("database.db")
    conexao.row_factory = sqlite3.Row
    return conexao

sqlite.execute("""CREATE TABLE IF NOT EXISTS livros(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               titulo STRING NOT NULL,
               autor STRING NOT NULL,
               genero STRING,
               paginas INTEGER NOT NULL,
               status STRING NOT NULL,
               nota INTEGER,
               data_inicio TEXT NOT NULL,
               data_termino TEXT)""")

conexao.commit()
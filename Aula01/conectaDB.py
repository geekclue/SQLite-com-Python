#conectaDB.py

import sqlite3
from sqlite3 import Error

def conectar(db_path):
    conexao = None
    try:
        conexao = sqlite3.connect(db_path)
    except Error as err:
        print(f"Erro ao conectar o banco de dados {db_path}.")
    return conexao

def desconectar(conexao = None):
    if conexao is not None:
        conexao.close()

conexao = conectar("clubeLivro.db")
desconectar(conexao)

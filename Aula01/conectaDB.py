#File: conectaDB.py
import os
import sqlite3

def conectar(db_path):
    conexao = None
    try:
        if not os.path.exists(db_path):
            conexao = sqlite3.connect(db_path, timeout=20)

    except sqlite3.DatabaseError as err:
        print(f"Erro ao conectar o banco de dados {db_path}.")
    
    return conexao


def desconectar(conexao = None):
    if conexao is not None:
        conexao.close()

conexao = conectar("clubeLivro.db")
desconectar(conexao)
import sqlite3

DATABASE_NAME = "contratos.db"

def conectar():

    conn = sqlite3.connect(DATABASE_NAME)

    return conn
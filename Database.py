import sqlite3
import os

DATABASE = "instance/chamados.db"

def conectar():
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_banco():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            solicitante TEXT NOT NULL,
            titulo TEXT NOT NULL,
            escricao TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Aberto',
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )   
    """)

    conexao.commit()
    conexao.close()
    


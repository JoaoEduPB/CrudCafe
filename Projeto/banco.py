import sqlite3 as sql

def criar_tabela():
    con = sql.connect("cafe.db")
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
    )
    """)

def inserir_dados(nome=str, preco=float, qtd=int):
    con = sql.connect("cafe.db")
    cur = con.cursor()
    
    entrada = (nome, preco, qtd)
    cur.execute('''
    INSERT INTO estoque (nome, preco, quantidade)
    VALUES (?,?,?)
    ''', entrada)
    con.commit()
    con.close()

def vizualizar():
    con = sql.connect("cafe.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM estoque")
    dados = cur.fetchall()
    for dado in dados:
        print(dado)
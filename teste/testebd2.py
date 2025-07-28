import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "database.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "clientes"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


cursor.execute(
    f"INSERT INTO {TABLE_NAME} (nome, idade, endereço, CEP,  bairro)VALUES"
    "('anderson', 12, 'rua padre nino mirald', 265621380, 'jacutinga'), "
    "('martha', 30, 'rua manoel afonso ', 26562120, 'Centro')"
)
connection.commit()
cursor.execute(
    "INSERT INTO 'produtos' (codigo, quantidade, valor, vendas)VALUES"
    "('200', 12, '300,00', 265), "
    "('201', 30, '20,00', 320)"
)
connection.commit()


cursor.close()
connection.close()

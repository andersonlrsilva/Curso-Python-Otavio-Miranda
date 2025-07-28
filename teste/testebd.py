import sqlite3
from pathlib import Path

# informação do banco de dados
ROOT_DIR = Path(__file__).parent
DB_NAME = "database.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "clientes"

# conectando ao banco de dados
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS 'clientes'"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "nome TEXT,"
    "idade INT,"
    "endereço TEXT,"
    "CEP INT,"
    "bairro TEXT"
    ")"
)
connection.commit()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS 'produtos'"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "codigo INT,"
    "quantidade INT,"
    "valor FLOAT,"
    "vendas INT"
    ")"
)
connection.commit()


# fechando banco de dados
cursor.close()
connection.close()

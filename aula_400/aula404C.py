# EVITANDO SQL INJECTION


import os
from unittest import result
import dotenv
import pymysql

TABLE_NAME = 'customers'

dotenv.load_dotenv()
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)

cursor = connection.cursor()


# CRIANDO A TABELA COSTUMERS
with connection.cursor() as cursor:
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
        'id INT NOT NULL AUTO_INCREMENT,  '
        'nome VARCHAR(50) NOT NULL, '
        'idade INT NOT NULL, '
        'PRIMARY KEY  (id)'
        ')'
    )
    cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

# INICIANDO A MANIPULAÇÃO DE DADOS

with connection.cursor() as cursor:
    sql = (
        f'INSERT INTO {TABLE_NAME} '
        '(nome, idade) VALUES (%s, %s) '
    )
    data = ('luiz', 18)
    result = cursor.execute(sql, data)
    print(sql, data)
    print(result)
connection.commit()

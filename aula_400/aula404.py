
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='maidem',
    database='base_de_dados'
)

cursor = connection.cursor()


# fechando a conexão
cursor.close()
connection.close()

import sqlite3

from main import DB_FILE, DB_NAME, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name = "QALQUER", weight=67.89 '
    'WHERE id =2'

)

connection.commit()

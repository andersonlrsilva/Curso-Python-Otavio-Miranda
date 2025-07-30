
import sqlite3
from main import DB_FILE, DB_NAME, TABLE_NAME, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'DELETE FROM {TABLE_NAME} '
               'WHERE id = "1"')

cursor.execute(f'DELETE FROM {TABLE_NAME} '
               'WHERE id = "3"')

connection.commit()

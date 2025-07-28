import sqlite3

from testebd import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f"DELETE FROM {TABLE_NAME}")
connection.commit()

cursor.close()
connection.close()

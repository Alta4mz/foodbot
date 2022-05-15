import sqlite3


def createTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_menu.db")
        cursor = sqlite_connection.cursor()
        sqlite_create_table_query = '''CREATE TABLE food (
                                               id INTEGER PRIMARY KEY,
                                               food_type TEXT NOT NULL,
                                               food_name TEXT NOT NULL,
                                               food_composition TEXT NOT NULL);'''
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с SQLite возникла ошибка: ", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение закрыто.")
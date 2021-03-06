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
def addFood(id, food_type, food_name, food_composition):
    try:
        sqlite_connection = sqlite3.connect("sqlite_menu.db")
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = '''INSERT INTO food
                                 (id, food_type, food_name, food_composition)
                                 VALUES
                                 (?, ?, ?, ?)'''
        data_tuple = (id, food_type, food_name, food_composition)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqlite_connection.commit()
        print("Запись добавлена в таблицу. ")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с SQLite возникла ошибка: ", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто. ")
def readTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_menu.db")
        cursor = sqlite_connection.cursor()
        sqlite_read_query = '''SELECT * FROM menu'''
        cursor.execute(sqlite_read_query)
        record = cursor.fetchall()
        sqlite_connection.commit()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Ошибка: ", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close

#createTable()
#addFood("1", "Пицца", "Пепперони", "Состав: моцарелла, фирменный соус, салями")
#addFood("2", "Пицца", "Карбонара", "Состав: моцарелла, ветчина, бекон, лук, фирменный соус ")
#addFood("3", "Пицца", "Пять сыров", "Состав: фета, пармезан, моцарелла, чеддер, голубой сыр")
#addFood("4", "Салат", "Цезарь", "Состав: курица, пармезан, кириешки), соус цезарь")
#addFood("5", "Салат", "Греческий", "Состав: овощи, оливковое масло")
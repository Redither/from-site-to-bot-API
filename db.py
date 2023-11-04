import sqlite3

def create_db():
    try:
        sqlite_connection = sqlite3.connect('db.sqlite')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")
        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def create_tickets_table():
    try:
        sqlite_connection = sqlite3.connect('db.sqlite')
        sqlite_create_table_query = '''CREATE TABLE tickets
                                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT,
                                        phone TEXT,
                                        message TEXT)'''
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite с пользователями создана")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def add_ticket(name, phone, message):
    try:
        sqlite_connection = sqlite3.connect('db.sqlite')
        cursor = sqlite_connection.cursor()
        # print("Подключено к SQLite")
        cursor.execute("INSERT INTO tickets (name, phone, message) VALUES (?, ?, ?)", (name, phone, message))
        sqlite_connection.commit()
        print("Пользователь зарегистрирован")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")

create_db()
create_tickets_table()
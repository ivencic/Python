import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('ich_edit.db')
cursor = conn.cursor()


# Функция для вывода строк таблицы
def display_table(t_name):
    try:
        # Запрос на получение всех строк из указанной таблицы
        cursor.execute(f"SELECT * FROM {t_name}")
        rows = cursor.fetchall()

        if len(rows) > 0:
            # Выводим все строки таблицы
            for row in rows:
                print(row)
        else:
            print("Таблица пуста")
    except sqlite3.OperationalError:
        print("Таблицы с таким названием не существует")


# Запрос у пользователя названия таблицы
table_name = input("Введите название таблицы: ")

# Выводим содержимое таблицы
display_table(table_name)

# Закрываем соединение с базой данных
conn.close()

"""
    Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его.
    При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен".
    Если файл не существует или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке.
"""

import sys
import subprocess


if len(sys.argv) != 2:
    print("Использование: python run_script.py <путь_к_файлу.py>")
else:
    file_path = sys.argv[1]
    try:
        result = subprocess.run(["python", file_path], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Файл '{file_path}' успешно запущен.")
        else:
            print(result.stderr)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Ошибка: Не удалось запустить файл '{file_path}': {e}")

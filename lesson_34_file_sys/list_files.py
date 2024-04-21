"""
Напишите программу, которая принимает в качестве аргумента командной строки путь к директории и
выводит список всех файлов и поддиректорий внутри этой директории.
Для этой задачи используйте модуль os и его функцию walk.
Программа должна выводить полный путь к каждому файлу и директории.

"""

import sys
import os


def list_files_and_subdirectories(direct_path):
    # Проверяем, существует ли указанная директория
    if not os.path.exists(direct_path):
        print(f"Директория '{direct_path}' не существует.")
        return

    for root, dirs, files in os.walk(direct_path):
        print(f"Директория: {root}")
        for file in files:
            file_path = os.path.join(root, file)
            print(f"  Файл: {file_path}")
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            print(f"  Поддиректория: {dir_path}")


directory_path = sys.argv[1]
list_files_and_subdirectories(directory_path)

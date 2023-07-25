# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt. После этого удалите созданную папку.
#  Все операции выполнять с помощью встроенных функций библиотеки os.
import os

# Путь к рабочему столу
desktop_path = os.path.expanduser(r"C:\Users\79183\Desktop")

# Создание папки
folder_path = os.path.join(desktop_path, "my_folder")
os.mkdir(folder_path)

# Создание текстовых файлов
file1_path = os.path.join(folder_path, "test_1.txt")
file2_path = os.path.join(folder_path, "test_2.txt")
file3_path = os.path.join(folder_path, "test_3.txt")

open(file1_path, "w").close()
open(file2_path, "w").close()
open(file3_path, "w").close()

# Переименование файлов
os.rename(file1_path, os.path.join(folder_path, "rename_1.txt"))
os.rename(file2_path, os.path.join(folder_path, "rename_2.txt"))
os.rename(file3_path, os.path.join(folder_path, "rename_3.txt"))

# Удаление папки
os.rmdir(folder_path)


from colorama import Fore, init
from pathlib import Path
import sys

init(autoreset=True)

def directory_struct(dir_path, ind=0):
    # Створюємо об'єкт Path для заданого шляху та перевірка на існування
    directory = Path(dir_path)
    # print(directory)
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + f"Шлях '{dir_path}' не існує або не є директорією.")
        return
    # Цикл обходу всіх піддиректорій та файлів у заданній директорії
    for item in directory.iterdir():
        if item.is_dir():
            print(" " * (ind+4) + Fore.BLUE + f"{item.name}/")
            directory_struct(item, ind+6)
        elif item.is_file():
            print(' '*(ind+4)+ Fore.YELLOW + f'{item.name}')


if len(sys.argv) != 2:
    print(Fore.RED + "Потрібно вказати шлях до директорії.")
    sys.exit(1)
        
# ttt='../Ревью_1'
try:
    path_param = sys.argv[1]
    first_dir=Path(path_param)
    # Перевірка наявності шляху із аргументу командного рядка
    if first_dir.exists():
        print(Fore.GREEN + f"{first_dir.name}/")
    else:
        print(Fore.RED + f"Шлях '{path_param}' не існує.")
        sys.exit(1)

    directory_struct(path_param)
# Перехват помилки при помилках
except Exception as e:
    print(f"Сталася помилка : {e}")

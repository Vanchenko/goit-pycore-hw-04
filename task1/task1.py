from pathlib import Path
import sys

def total_salary(path):
    # перевірка на існування файлу данних
    if not path.exists():
        print(f"Файл даних {path} не існує!")
        sys.exit()
    try:  
        with open(path,encoding='utf-8') as file:
            # ініціація змінних початковими значеннями
            sum_salary = 0
            count = 0
            average_salary = 0
            # цикл читання і обробки даних із файлу
            for line in file:
                str_date = line.split(',')
                str_date = [s.rstrip('\n') for s in str_date]
                sum_salary = sum_salary + int(str_date[-1])
                count +=1
    # перехоплення помилки при читанні данних із файлу
    except Exception as e:
        print(f"Помилка в даних файла: {e}")
        exit()
    # розрахунок середньої ЗП розробника
    average_salary = sum_salary/count
    return sum_salary, average_salary
# шлях та ім'я файлу даних
filepath = Path(__file__).parent / 'salary.txt'

total, average = total_salary(filepath)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.0f}")

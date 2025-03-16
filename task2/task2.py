from pathlib import Path

def get_cats_info(path):
    # перевірка на існування файлу данних
    if not path.exists():
        print(f"Файл даних {path} не існує!")
        exit()
    try:
        with open(path,encoding='utf-8') as file:
            # ініціація змінних початковими значеннями
            result_dict=[]
            # цикл читання і обробки даних із файлу
            for line in file:
                str_date = line.split(',')
                str_date = [s.rstrip('\n') for s in str_date]
                # формування та додавання до списку окремого словника
                result_dict.append({
                    'id':str_date[0],
                    'name':str_date[1],
                    'age':str_date[2]
                })
    # перехоплення помилки при читанні данних із файлу
    except Exception as e:
        print(f"Помилка в даних файла: {e}")
        exit()
        # print(result_dict)
    return result_dict                
# шлях та ім'я файлу даних            
filepath = Path(__file__).parent / 'cats_file.txt'
cats_info = get_cats_info(filepath)
print(cats_info)

# виведення словників зі списку у стобчик - зручно перевіряти результат
# print(*cats_info, sep="\n")
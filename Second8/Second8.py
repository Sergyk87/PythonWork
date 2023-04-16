# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии и изменить данные\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice


def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data


def full_list(data: list):
    for elem in data:
        for k, v in elem.items():
            print(f'{k}: {v}')
        print()


def find_last_name(data):
    last_name = input("Введите фамилию: ")
    for elem in data:
        if last_name in elem["Фамилия"]:
            for k, v in elem.items():
                print(f'{k}: {v}')
            print()


def find_number(data):
    number = input("Введите номер телефона: ")
    for elem in data:
        if number in elem["Телефон"]:
            for k, v in elem.items():
                print(f'{k}: {v}')
            print()


def add_abonent(filename):
    last_name = input('Ведите фамилию: ')
    first_name = input('Ведите имя: ')
    phone = input('Введите телефон: ')
    desc = input('Ведите описание: ')
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'{last_name},{first_name},{phone},{desc}\n')
    

def save_txt(data):
    with open(input("Введите имя файла: "), 'w', encoding='utf-8') as new_file:
        for i in data:
            str_i = ""
            for v in i.values():
                str_i += v + ","
            str_i = str_i[:-1]
            new_file.write(str_i + "\n")


spisok = read_csv("phonebook.csv")
filename = 'phonebook.csv'

choise = 0
while choise != 6:
    choise = show_menu()
    if choise == 1:
        full_list(spisok)
    elif choise == 2:
        find_last_name(spisok)
    elif choise == 3:
        find_number(spisok)
    elif choise == 4:
        add_abonent(filename)
    elif choise == 5:
        save_txt(spisok)

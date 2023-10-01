# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

def enter_first_name(): 
    return input("Введите имя абонента: ").title() 


def enter_second_name():
    return input("Введите фамилию абонента: ").title()


def enter_phone_number():
    return input("Введите номер телефона: ")


def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    number = enter_phone_number()
    with open('book.txt', 'a', encoding = 'utf-8') as file:    
        file.write(f'{name} {surname}\n{number}\n\n')  


def changes_data():
    with open("book.txt", "r", encoding="utf-8") as data:
        old_data = data.read()
        print(old_data)
        index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
        old_data_lines = old_data.split("\n")
        edit_old_data_lines = old_data_lines[index_delete_data]
        elements = edit_old_data_lines.split(" ")
        first_name = enter_first_name()
        second_name = enter_second_name()
        phone = input(f"Введите номер телефона: {enter_phone_number}")
        num = elements[0]
        if len(first_name) and len(second_name) == 0:
            first_name == elements[1]
            second_name == elements[1]
        if len(phone) == 0:
            phone == elements[2]
        edited_line = f"{num} {first_name} {second_name} {phone}"
        old_data_lines[index_delete_data] = edited_line
        print(f"Запись - {edit_old_data_lines}, изменена на - {edited_line}\n")
        with open("book.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(old_data_lines))

                
        
def print_data():
    with open('book.txt', 'r', encoding = 'utf-8') as file:
        print(file.read())


def search_line():
    print("Выберите вариант поиска:\n"
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Телефон')
    index = int(input('Введите вариант: ')) - 1 
    searched = input('Ввести поисковые данные: ').title()
    with open('book.txt', 'r', encoding = 'utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:          
            new_item = item.replace('\n', ' ').split()  
            if searched in new_item[index]:
                print(item, end="\n\n")        

def delete_data():
    with open("book.txt", "r", encoding="utf-8") as data:
        tel_book = data.read()
        index_delete_data = int(input("Введите номер строки для удаления: \n")) - 1
        tel_book_lines = tel_book.split("\n")
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        print(f"Удалена запись: {del_tel_book_lines}\n")
        with open("book.txt", "w", encoding="utf-8") as data:
            data.write("\n".join(tel_book_lines))

 

def interface():
    cmd = 0
    while cmd != '6':
        print("Выберите действие:\n"
            '1. Добавить контакт\n'
            '2. Изменить контакт\n'
            '3. Вывести все контакты\n'
            '4. Поиск контакта\n'
            '5. Удалить контакт\n'
            '6. Выход')
        cmd = input("введите действие: ")
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print("Некорректный ввод")
            cmd = input("Введите действие: \n")
        match cmd: 
            case '1': 
                enter_data()
            case '2':
                changes_data()
            case '3':
                print_data()
            case '4':
                search_line()
            case '5':
                delete_data()
            case '6':
                print('Всего доброго! ')

                
interface()
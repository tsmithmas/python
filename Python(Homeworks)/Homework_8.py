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
def enter_changes_name(): 
    return input("Введите изменения: ").title()   
def changes():
    change = enter_changes_name()
    with open('book.txt', 'a', encoding = 'utf-8') as file:    
        file.write(f'{change}\n\n') 
print(f'Изменено на {changes}')
                
        
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

# def delete_data():

 

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
            cmd = input("Введите действие: ")
        match cmd: 
            case '1': 
                enter_data()
            case '2':
                changes_data()
            case '3':
                print_data()
            case '4':
                search_line()
            # case '5':
            #     delete_data()
            case '6':
                print('Всего доброго! ')

                
interface()
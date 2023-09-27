# Задача 55
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, 
# номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def enter_first_name():  # def enter_first_name(msg: str)  msg - это переменная, str - это подсказка, чтобы PyCharm  не ошибался 
    return input("Введите имя абонента: ").title() # .title() - делает первую букву вводимого млова заглавной


def enter_second_name():
    return input("Введите фамилию абонента: ").title()


def enter_family_name():
    return input("Введите отчество абонента: ").title()


def enter_phone_number():
    return input("Введите номер телефона: ")


def enter_address_number():
    return input("Введите адрес абонента: ").title() 

def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding = 'utf-8') as file:    # a - сокращенно от append добавлять, прибавлять
        file.write(f'{name} {surname} {family}\n{number}\n{address}\n\n')   # \n - отступ на строку

        
def print_data():
    with open('book.txt', 'r', encoding = 'utf-8') as file: # r - read считывать, читать
        print(file.read())


def search_line():
    print("Выберите вариант поиска:\n"
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант: ')) - 1 # чтобы отсчет шел от нуля
    searched = input('Ввести поисковые данные: ').title()
    with open('book.txt', 'r', encoding = 'utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:             # для каждого нашего объекта item в списке data
            # if searched in item[index]:      # Если у нас введенная информация пользователя(searched) есть в нашем объекте(item)
            new_item = item.replace('\n', ' ').split()    # эта строчка разделила значения в списке 
            if searched in new_item[index]:
                print(item, end="\n\n")           # Тогда мы печатаем наш объект item из списка data
        # file.seek(0)                 # seek вызывает со значения(символа в строке) по заданному индексу
        # print(file.readlines())      # readlines - считывает данные построчно, разбивает список на строки(перенос строки)
 

def interface():
    cmd = 0
    while cmd != '4':
        print("Выберите действие:\n"
            '1. Добавить контакт\n'
            '2. Вывести все контакты\n'
            '3. Поиск контакта\n'
            '4. Выход')
        cmd = input("введите действие: ")
        while cmd not in ('1', '2', '3', '4'):
            print("Некорректный ввод")
            cmd = input("Введите действие: ")
        match cmd: 
            case '1': 
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                print('Всего доброго! ')

                
interface()


    

    


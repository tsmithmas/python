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
    return input("Введите имя абонента: ")

def enter_second_name():
    return input("Введите фамилию абонента: ")

def enter_family_name():
    return input("Введите отчество абонента: ")

def enter_phone_number():
    return input("Введите номер телефона: ")

def enter_address_number():
    return input("Введите адрес абонента: ")

def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding = 'utf-8') as file:    # a - сокращенно от append
        file.write(f'{name} {surname} {family}\n{number}\n{address}')
        

enter_data()
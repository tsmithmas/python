# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.
# Пример:

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

# a = int(input('Введите число a \n'))
# b = int(input('Введите числ b \n'))

# def f(a, b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     elif b < 0:
#         return 1 / f(a, -b)
#     else:
#         return a * f(a, b-1)

# print(f(a, b))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.
# Пример:

# sum(2, 2)
# # 4

# a = int(input("Введите первое неотрицительное число "))
# b = int(input("Введите второе неотрицательно число "))

# def sum(a, b):
#     if a == 0:
#         return b
#     else:
#         return sum(a-1, b+1)


# print(sum(a, b))
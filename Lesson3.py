def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)
a = sum_numbers
print(a)

def sum_str(*args):  # переменная args, * означает неограниченное количество передаваемых аргументов
    res = ''         # создали переменную res, которая имеет тип данных строка
    for i in args:   # проходим по всем значениям переменной 
        res += i     # при каждой итерации к переменной res добавляем i
    return res       # возвращаем переменную
print(sum_str('q','e','l'))

import modul1
print(modul1.max1(5, 9))  # вызываем функцию max1 из файла modul1

from modul1 import max1
print(max1(5, 9))         # тоже самое

from modul1 import *      # если поставить * то импортируем из файла все функции

import modul1 as m1       # импортируем модуль как имя m1, для более простого написания в дальнейшем
print(m1.max1(5, 9))


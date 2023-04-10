# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint as rnd
n = int(input('Введите количество жлементов: '))
list1 = [rnd(-10, 10) for _ in range(n)]
print(list1)

rezult_list = []
n_min = int(input('Введите минимум: '))
n_max = int(input('Введите максимум: '))
for i in range(n):
    if n_min <= list1[i] <= n_max:
        rezult_list.append(i)

print(rezult_list)


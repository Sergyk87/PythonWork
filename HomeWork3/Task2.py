# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
n = int(input("Введите количество элементов: "))
list = list()
for i in range(n):
    list.append(randint(1, 10))
print(list)
x = int(input("Задайте число: "))
number = 0
for i in list:
    if abs(x - i) < abs(x - number) and abs(x - i) != 0:
        number = i
print(f"-> {number}")

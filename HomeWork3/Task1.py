# Задача 16: 
#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint
n = int(input("Введите количество элементов: "))
x = int(input("Задайте число: "))
list = list()
for i in range(n):
    list.append(randint(1,10))
print(list)
count = 0
for i in list:
    if i == x:
        count += 1
print(count)

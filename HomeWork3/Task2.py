# Задача 18: 
#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
a = []
n = int(input("Введите количество элементов: "))
x = int(input("Задайте число: "))
for i in range(n):
    a.append(randint(1,10))
print(a)
j = 0
find_res = 0
flag = True
while find_res == 0:
    i = 0
    while i<n and flag:
        if abs(x-a[i])==j:
            find_res = a[i]
            flag = False
        i+=1
    j+=1

print(f'res = {find_res}')
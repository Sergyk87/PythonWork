# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('введите первый элемент: '))
n = int(input('введите количество элементов: '))
d = int(input('введите разность: '))
list1 = []
for i in range(n):
    list1.append(a1 + i * d)
print(list1)
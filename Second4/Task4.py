# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка,стоящих на нечётной позиции
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
# n = int(input('введите количество элементов: '))
# list = list()
# for i in range(n):
#     list.append(randint(1, 10))
# print(list)
# sum = 0
# for i in range(len(list)):
#     if i % 2 != 0:
#         sum += list[i]
# print(sum)


# from random import randint

# n = int(input('Введите кол-во элементов: '))

# list = [randint(0, 10) for i in range(n)]
# print(list)

# print(sum([list[i] for i in range(1, len(list), 2)]))  #range идет по индексам(начинаем с 1, len(list) до конца списка, шаг 2)

my_list = [8, 5, 7, 3, 6]
print(sum(my_list[1::2]))  # с первого до последнего с шагом 2
# Задача No3. Решение в группах
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

# a = int(input('Кол-во учащихся 1 класса: '))
# b = int(input('Кол-во учащихся 2 класса: '))
# c = int(input('Кол-во учащихся 3 класса: '))
#
# sum = 0
# for i in a, b, c:
#     k = i / 2
#     if k % 2 == 0:
#         print(f'{int(k)}')
#         sum = sum + int(k)
#     else:
#         print(f'{int(k) + 1}')
#         sum = sum + int(k) +1
# print(f"Мин. кол-во парт: {sum}")

n1 = int(input("Введите количество учащихся в классе 1: "))
n2 = int(input("Введите количество учащихся в классе 2: "))
n3 = int(input("Введите количество учащихся в классе 3: "))

# result = ((n1 // 2 + (n1 % 2 != 0)) + (n2 // 2 + (n2 % 2 != 0)) + (n3 // 2 + (n3 % 2 != 0)))

result = (n1 + 1) // 2 + (n2 + 1) // 2 + (n3 + 1) // 2

print(f"-> Наименьшее требуемое число парт: ", result)



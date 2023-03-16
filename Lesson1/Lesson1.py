# a = 5
# b = 3.25
# c = "hello"
# print(a,"-", b,"-", c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# print("Введите первое число: ")
# a = int(input())
# b = int(input("Введите второе число: "))
# print(a, "+", b, "=", a + b)

# c = 5.89
# print(c)
# n = int(c)
# print(n)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# a = 5.3659
# b = 6.3548
# print(round(a*b, 3))   #round в аргументах сначала указываем число, а затем число знаков, которые нужно оставить после запятой

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# a = "qwerty" #строка а
# print(a[0])  #вывод на печать элемента строки
# for i in a:
#   print(i) #вывод всех элементов по очереди

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))  #определяет длинну строки
# print('ещё' in text) #ищет есть или нет в тексте(true или false)
# print(text.lower())  #перевод всего текста в нижний регистр
# print(text.upper())  #перевод всего текста в верхний регистр
# print(text.replace('ещё' , 'ЕЩЁ'))  #замена текста в строке на аргумент из скобок
# print(text[len(text) - 1])  #выведет последнюю букву текста
# срезы
# print(text[-1])             #выведет последнюю букву текста
# print(text[:])              #выводит все символы
# print(text[:2])             #выводит элементы с нулевого по второй(не включая)

# Найти большее число из двух

# Найти большее число из двух

a = int(input('Число А ='))

b = int(input('Число Б ='))

print(a == b)

if a > b:
    print(f"большее число a = {a}")
elif a == b:
    print("a == b")
else:
    print(f"большее число b = {b}")
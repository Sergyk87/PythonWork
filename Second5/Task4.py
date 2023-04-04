# Задача №37. 
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы(даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def reverse(a):
    if len(a) == 0:
        return ''
    else:
        return str(reverse(a[1:])) + a[0]
    
n = input('Введите последовательность: ')
print(reverse(n))
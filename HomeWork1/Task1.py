# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = int(input("Введите трехзначное число: "))
if a > 99 and a < 1000:
    print(f"{a} -> {a//100 + (a%100)//10 + a%10} ({a//100} + {(a%100)//10} + {a%10})")
else:
    print(" Число не является трехзначным, попробуйте еще раз!")


# РЕШЕНИЕ ЧЕРЕЗ СТРОКУ
# number = input("Введите любое трехзначное число ")
# sumOfDigits = int(number[0]) + int(number[1]) + int(number[2])
# print(f"Сумма цифр введенного числа = {sumOfDigits} ")         
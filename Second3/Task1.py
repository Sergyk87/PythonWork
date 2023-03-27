# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6


#mass = [1, 1, 2, 0, -1, 3, 4, 4]
#print(len(set(list))) # решение в одну строку, перевод списка во множество(во множестве только уникальные )

mass = input().split()
new_mass = []
for i in mass:
    if i not in new_mass:
        new_mass.append(i)
print(len(new_mass))


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]  # создаем переменую, в нее записываем первое значение
    less = [i for i in array[1:] if i <= pivot]  # проходим циклом по списку не включая первое значение и записываем в массив все, что пеньше первого значения
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)  # pivot взяли в скобки для преобразования в список, т.к. число и списки не складываются

print(quick_sort([2,36,214,45,21,58,6,3,541,1,42,22]))
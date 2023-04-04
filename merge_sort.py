# Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1:         # будем делить список пополам с помощью срезов
        mid = len(nums) // 2  # создаем переменную и берем только целую часть от деления(это середина)
        left = nums[:mid]     # от начала до середины
        right = nums[mid:]    # от середины до конца
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [2,5,3,1,5,4,56,6,3,4,7,8,6,9]
merge_sort(list1)
print(list1)
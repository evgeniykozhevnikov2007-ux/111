def sum_even_index_times_last(arr):
    if not arr:  # проверка на пустой массив
        return 0

    s = 0
    for i in range(0, len(arr), 2):  # идём по четным индексам
        s += arr[i]

    return s * arr[-1]  # умножаем на последний элемент

# Примеры
print(sum_even_index_times_last([0, 1, 7, 2, 4, 8]))  # 88
print(sum_even_index_times_last([1, 3, 5]))           # 30
print(sum_even_index_times_last([6]))                 # 36
print(sum_even_index_times_last([]))                  # 0

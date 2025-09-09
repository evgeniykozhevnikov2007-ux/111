def split_list(lst):
    if not lst:  # пустой список
        return [[], []]
    mid = (len(lst) + 1) // 2  # если нечётное, первый список больше
    return [lst[:mid], lst[mid:]]

# Проверка работы на примерах
print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))
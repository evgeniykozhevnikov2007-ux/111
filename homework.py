def move_last_to_first(lst):
    if len(lst) > 1:
        lst.insert(0, lst.pop())
    return lst

# Проверка работы на примерах
print(move_last_to_first([12, 3, 4, 10]))
print(move_last_to_first([1]))
print(move_last_to_first([]))
print(move_last_to_first([12, 3, 4, 10, 8]))

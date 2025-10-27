numbers = [0, 1, 0, 12, 3]

# создаём новый список без нулей
no_zeros = []
zeros = 0
for n in numbers:
    if n != 0:
        no_zeros.append(n)
    else:
        zeros += 1

# добавляем нули в конец
for _ in range(zeros):
    no_zeros.append(0)

numbers = no_zeros
print(numbers)

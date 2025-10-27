import random

numbers = [random.randint(0, 20) for _ in range(random.randint(3, 10))]
print(numbers)

new_list = [numbers[0], numbers[2], numbers[-2]]
print(new_list)

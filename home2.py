def sum_even_index_times_last(arr):
    if not arr:
        return 0

    s = 0
    for i in range(0, len(arr), 2):
        s += arr[i]

    return s * arr[-1]


print(sum_even_index_times_last([0, 1, 7, 2, 4, 8]))
print(sum_even_index_times_last([1, 3, 5]))
print(sum_even_index_times_last([6]))
print(sum_even_index_times_last([]))
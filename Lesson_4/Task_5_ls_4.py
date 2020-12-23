# Task_5

from functools import reduce


def new_list(acc, x):
    return acc * x


my_list = [i for i in range(100, 1001) if i % 2 == 0]
composition = reduce(new_list, my_list)
print(f"Список: {my_list}")
print(f"Произведение чисел из списка: {composition}")
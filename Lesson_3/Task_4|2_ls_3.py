# Task_4/2

def my_func(x, y):

    if y < 0:
        y *= -1
    n = x
    for i in range(1, y):
        x *= n
    print(1 / x)


my_func(2, -5)
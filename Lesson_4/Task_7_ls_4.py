# Task_7

def factorial(n):
    step = 1
    for i in range(1, n + 1):
        step *= i
        yield step


n = 5
for el in factorial(n):
    print(el)
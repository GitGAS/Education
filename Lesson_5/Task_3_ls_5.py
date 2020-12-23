# Task_3

with open("Task_3.txt") as file:
    salary = []
    min_solary = []
    my_list = file.read().split('\n')

    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            min_solary.append(i[0])
        salary.append(i[1])

print(f'Оклад меньше 20000: {min_solary}\nCредний оклад: {sum(map(int, salary)) / len(salary):.2f}')

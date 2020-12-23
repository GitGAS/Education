# Task_2

with open("Task_2.txt") as file:

    lines_num = 0
    for lines in file:
        lines_num += 1

with open("Task_2.txt") as file:

    words = str(file.readlines())

    print(f"Количество слов: {len(words.split())}\nКоличество строк: {lines_num}")

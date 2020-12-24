# Task_5

file = open(file = "Task_5.txt", encoding = "UTF-8", mode = "wt")
file.write("1 2 3 4 5")
file.close()

with open("Task_5.txt") as file:
    file = file.readline()
    num = 0

for i in range(len(file)):
    if file[i] != " ":
        num = num + int(file[i])

print(f"Cумма чисел в строке: {num}")









# Task_1

file = open(file = "Task_1.txt", encoding = "UTF-8", mode = "wt")

while True:
    user_txt = input("Введите строку: ")
    file.writelines(user_txt + "\n")
    if user_txt == "":
        break

file.close()


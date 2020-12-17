# Task_4

user_str = input("Введите несколько слов, разделённых пробелом: ")
str_number = 1
words = []

for i in range(user_str.count(' ') + 1):
    words = user_str.split()
    if len(str(words)) <= 10:
        print(f" {str_number} {words [i]}")
        str_number += 1
    else:
        print(f" {str_number} {words [i] [:10]}")
        str_number += 1
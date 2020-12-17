# Task_5

list = [4, 3, 8, 2, 1]
print(f"Рейтинг - {list}")


number = int(input("Введите число: "))


for i in range(len(list)):
    if list[i] == number:
        list.insert(i + 1, number)
        break
    elif list[0] < number:
        list.insert(0, number)
    elif list[-1] > number:
        list.append(number)
    elif list[i] > number and list[i + 1] < number:
        list.insert(i + 1, number)


print(f"Рейтинг - {list}")

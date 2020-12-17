# Task_5


def my_func():
    sum_num = 0
    leave = False

    while leave == False:
        list_num = input(" Для завершения программы нажмите Введите числа: ").split()
        num = 0
        for i in range(len(list_num)):
            if list_num[i] != "q" and list_num[i] != "q":
                num = num + int(list_num[i])
            else:
                leave = True
                break
        sum_num = sum_num + num
        print(f"Текущая сумма составляет: {sum_num}")
    print(f"Конечная сумма составляет: {sum_num}")

my_func()
# Task_3

seasons_lst = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите номер месяца от 1 до 12: "))

if month == 12 or month <= 2:
    print(seasons_dict.get(1))
    print(seasons_lst[0])
elif month == 3 or month <= 5:
    print(seasons_dict.get(2))
    print(seasons_lst[1])
elif month == 6 or month <= 8:
    print(seasons_dict.get(3))
    print(seasons_lst[2])
else:
    print(seasons_dict.get(4))
    print(seasons_lst[3])

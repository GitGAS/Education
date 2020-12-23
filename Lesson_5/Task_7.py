# Task_7

import json

with open(file="Task_7.txt") as file:
    av_profit = 0
    num_firms = 0
    new_list = []
    lst_firms = {}
    av_dict_profit = {}
    main_list = []

    for line in file:
        new_list.append(line.split())

    for i in new_list:
        x = 0
        x = int(i[2]) - int(i[3])
        if x > 0:
            lst_firms[i[0]] = x
            av_profit = av_profit + x
            num_firms += 1
        else:
            lst_firms[i[0]] = x
    av_dict_profit['Средняя выручка'] = round(av_profit/num_firms)

main_list.append(lst_firms)
main_list.append(av_dict_profit)

with open(file="Task_7.json", encoding="UTF-8", mode="w") as file:
    json.dump(main_list, file)
# Task_6



positions = int(input("Введите количество позиций товаров: "))
position_number = 1


new_dict = []
new_lst = []
new_analytic = {}


while position_number <= positions:
    new_dict = dict(dict(название=input("Введите название: "),
                         цена=input("Введите цену: "),
                         количество=input("Введите количество "),
                         ед=input("Введите единицу измерения: ")))
    new_lst.append((position_number, new_dict))
    position_number += 1

    new_analytic = dict({"название": new_dict.get("название"),
                         "цена": new_dict.get("цена"),
                         "количество": new_dict.get("количество"),
                         "ед": new_dict.get("ед")})
print(new_lst)

for key, value in new_analytic.items():
    print(key, value)

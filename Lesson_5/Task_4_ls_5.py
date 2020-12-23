# Task_4

txt_dict = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}

with open("Task_4.txt") as file:
    txt_list = file.readlines()
    txt_list = [i.split() for i in txt_list]

for i in txt_list:
    if i[0] in txt_dict.keys():
        i[0] = txt_dict[i[0]]

txt_list = [f"{i[0]} {i[1]} {i[2]} \n" for i in txt_list]

file = open(file = "Task_4_new.txt", encoding= "UTF-8", mode = "w")
file.writelines(txt_list)
file.close()

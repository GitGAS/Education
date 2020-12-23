# Task_6

def num(input_str):
    result = ""
    for i in range(len(input_str)):
        try:
            int(input_str[i])
            result += input_str[i]
        except ValueError:
            result += " "
    result = result.split()
    return result

def sum(list):
    result = 0
    for i in list:
        result += int(i)
    return result

new_dict = {}

with open("Task_6.txt") as file:
    list = file.readlines()

for i in list:
    new_dict[i.split()[0]] = sum(num(i))

print(new_dict)
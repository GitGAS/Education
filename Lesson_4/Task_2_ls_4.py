# Task_2

x = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = []

for i in range(len(x)-1):
    if x[i] < x[i + 1]:
        my_list.append(x[i+1])

print(my_list)
    
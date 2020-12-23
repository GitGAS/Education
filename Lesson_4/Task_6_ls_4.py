# Task_6

from itertools import count, cycle

it_1 = count(3)
for i in it_1:
    if i > 10:
        break
    print(i)

my_list = ["a", "b", "c", ]
it_2 = cycle(my_list)
step = 0
for i in it_2:
    step += 1
    if step == 10:
        break
    print(i)
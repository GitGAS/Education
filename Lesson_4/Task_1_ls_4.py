# Task_1

def zp():
    time = float(input("выработка в часах : "))
    t_cost = float(input("ставка в час: "))
    bonus = float(input("премия: "))
    sum = time*t_cost+bonus
    return sum

print(zp())

revenue = int(input("Введите сумму выручки (руб.): "))
costs = int(input("Введите сумму издержек (руб.): "))
loss = costs - revenue
profit = revenue - costs

if revenue < costs:
    print(f"Ваши убытки составляют: {loss} руб.")
elif revenue > costs:
    profitability = (profit/revenue)*100
    print(f"Ваша прибыль сотавляет: {profit} руб.")
    print(f"Рентабельность предприятия:  {profitability} %")
    employees = int(input("Введите колличество сотрудников вашей организации: "))
    profit_one_employee = profit / employees
    print(f"Прибыль в расчете на одного сотрудника составляет: {profit_one_employee:.2f} руб.")

# Task_1


def division():
    while True:
        try:
            a = int(input("Введите число a: "))
            b = int(input("Введите число b: "))
            div_result = a / b
        except ZeroDivisionError:
            print("Деление на ноль невозможно!")
            continue
        except ValueError:
            print("Ошибка ввода!")
            continue
        print(f"Результат: {div_result:.02f}")

division()


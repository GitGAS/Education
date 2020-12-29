# Task_4

class Car:

    def go(self):
        return f"{self.name} начал движение"

    def stop(self):
        return f"{self.name} остановился"

    def turn_right(self):
        return f"{self.name} поворачивает вправо"

    def turn_left(self):
        return f"{self.name} поворачивает влево"

    def print_speed(self):
        return f"Скорость {self.name} {self.speed}."


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police =is_police

    def print_speed(self):
        print(f"Скорость {self.name} {self.speed}.")

        if self.speed > 60:
            return f"Скорость {self.name} выше разрешенной!"
        else:
            return f"Скорость {self.name} допустимая скорость."

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def print_speed(self):
        print(f"Скорость {self.name} {self.speed}.")

        if self.speed > 40:
            return f"Скорость {self.name} выше разрешенной!"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def police(self):
        if self.is_police:
            return f"{self.name} автомобиль Полиции."
        else:
            return f"{self.name} не полицейский автомобиль."


bmw = SportCar(60, "Черный", "BMW", False)
mercedes = TownCar(30, "Красный", "Mercedes", False)
kamaz = WorkCar(70, "Ораньжевый", "Камаз", False)
lada = PoliceCar(110, "Белая", "Lada", True)
print(f"{kamaz.turn_left()}.")
print(f"{mercedes.turn_right()}.\n{kamaz.stop()}.")
print(f"{kamaz.color} {kamaz.name}.")
print(f"{kamaz.go()}.")
print(kamaz.print_speed())
print(f"{bmw.name} автомобиль Полиции? {bmw.is_police}")
print(bmw.print_speed())
print(mercedes.print_speed())
print(lada.police())
print(lada.print_speed())
# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля.
#
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.

class Car:
    def __init__(self, speed:int, color:str, name:str, is_police:bool=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} машина {self.name} поехала")

    def stop(self):
        print(f"{self.color} Машина {self.name} остановилась")

    def turn(self,direction):
        print(f"{self.color} Машина {self.name} повернула  {direction}")

    def show_speed(self):
        print(f"Машина {self.name}. Скорость: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed>60:
            print(f"Превышение огран. скорости 60 км/ч: {self.speed}")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed>60:
            print(f"Превышение огран. скорости 40 км/ч: {self.speed}")

class PoliceCar(Car):
    pass


townCar = TownCar(100, "Черная", "рабочая машина")
townCar.go()
townCar.turn("Направо")
townCar.stop()
townCar.show_speed()

sportCar = SportCar(100, "зеленая", "Спортивная")
sportCar.go()
sportCar.turn("Направо")
sportCar.stop()
sportCar.show_speed()

workCar = WorkCar(100, "Красная", "рабочая машина")
workCar.go()
workCar.turn("Направо")
workCar.stop()
workCar.show_speed()

policeCar = PoliceCar(100, "белая", "полицейская машина",True)
policeCar.go()
policeCar.turn("Направо")
policeCar.stop()
policeCar.show_speed()








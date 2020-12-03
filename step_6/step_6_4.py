
class Car:

    def __init__(self, speed, grad):

        self.speed = speed
        self.color = "Blue"
        self.name = 'Dodge'
        self.is_police = False
        self.grad = grad

    def go(self):
        if self.speed > 0:
            print('Машина едет')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self):
        if 155 > self.grad > 90:
            print('Поворот на право')
        elif 25 < self.grad < 90:
            print('Машина поворачивает на лево')
        elif self.grad == 90:
            print("Машина едет прямо")
        else:
            print("Передние колеса сломаны")

    def show_car(self):
        print(f'Скорость - {self.speed}')


class TownCar(Car):

    def __init__(self, speed, grad):
        super().__init__(speed, grad)

        self.name = "Dodge"
        self.color = 'Black'

        if self.speed > 60:
            print('Обнаружено превышение скорости')

class SportCar(Car):

        def __init__(self, speed, grad):
            super().__init__(self, speed, grad)

            self.name = "Dodge Viper"
            self.color = 'Blue'


class WorkCar(Car):

    def __init__(self, speed, grad):
        super().__init__(self, speed, grad)
        self.name = "Dodge"
        self.color = 'Gray'

        if self.speed > 40:
            print('Обнаружено превышение скорости')

class PoliceCar(Car):

    def __init__(self, speed, grad):
        super().__init__(speed, grad)

        self.name = "Dodge"
        self.color = 'White-Black'


i = TownCar(150, 90)
print(i.name)
print(i.color)
print(i.show_car())
print(i.go())
print(i.turn())
print(i.stop())




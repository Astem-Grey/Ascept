
class Stationery:

    def __init__(self, title):

        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title}. Отрисовка синей тонкой линией')


class Pencill(Stationery):

    def draw(self):
        print(f'{self.title}. Запуск отрисовки серой средней линией')


class Handle(Stationery):

    def draw(self):
        print(f'{self.title}. Запуск отрисовки толстой черной линии')


i = Handle("Маркер")
i.draw()

a = Pen("Ручка")
a.draw()

i = Pencill("Карандаш")
i.draw()

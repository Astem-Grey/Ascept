
class Road:

    def __init__(self):
        self._lenght = 500
        self._width = 6

    def zatrat(self):
        all = self._lenght * self._width * 1 * 25
        return all

summ = Road()
print(summ.zatrat())
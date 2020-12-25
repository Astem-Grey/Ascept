
class Cell:

    def __init__(self, cell):
        # не понятный параметр, так как в вычислениях учавствуют только 2 клетки
        self.all_cell = 2
        self.cell = cell

    def __add__(self, other):
        self.result_cell = self.cell + other.cell
        return self.result_cell

    def __sub__(self, other):
        if self.cell < other.cell:
            print('Клетка слишком маленькая')
        else:
            self.result_cell = self.cell - other.cell
            return self.result_cell

    def __mul__(self, other):
        self.result_cell = self.cell * other.cell
        return self.result_cell

    def __truediv__(self, other):
        self.result_cell = self.cell // other.cell
        return self.result_cell

    def move_order(self):
        a1 = self.result_cell // 5
        a2 = self.result_cell % 5
        a = '*'
        if a2 != 0:
            b = (((a * 5) + '\\n') * a1) + ((a * a2) + '\\n')
        else:
            b = (((a * 5) + '\\n') * a1)
        print(f' Строка ячеек клетки = {b}')


an = Cell(26)
na = Cell(15)
print(an + na)
an.move_order()

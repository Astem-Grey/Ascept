

class Worker:

    def __init__(self, name, surname, position, income):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 50000, 'bonus': 20000}


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        full_name = (str(self.name) + ' ' + str(self.surname))
        return full_name

    def get_total_income(self):
        total_income = self._income + self.money.get('bonus')
        return total_income


a = Position("Кирилл", "Хотченко", 'Директор')
print(a.get_full_name())
print(a.get_total_income())

a = Position('Дмитрий', 'Негодуев', 'Прораб')
print(a.get_full_name())

# Раз 20 перечитал задане но так и не понял, нужно ли обновлять доход, при изменении имени сотрудника.
# В общем оставил так, если нужно добавлять напишите, я поправлю
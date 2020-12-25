
class Clothes:

    def __init__(self, name_clothers, clother_size):
        self.name_clothers = name_clothers
        self.clothers_size = clother_size

    def Coat(self):
        coat = self.clothers_size / 6.5 + 0.5
        return coat

    def Suit(self):
        siut = 2 * self.clothers_size + 0.3
        return siut

    def Clot(self):
        if self.name_clothers == 'Пальто':
            clote = self.Coat()
        else:
            clote = self.Suit()
        return clote


name = input('Введите название одежды: ')
size = int(input("Введите размер одежды: "))
clot = Clothes(name, size)
print(f'Понадобится {round(clot.Clot(), 2)}м ткани')
# if name == 'Пальто':
#     print(f'Для пошива пальто нужно {round(clot.Coat, 2)}м ткани')
# elif name == "Костюм":
#     print(f'Для пошива костюма нужно {round(clot.Suit, 2)}м ткани')
# else:
#     print('Вы ошиблись с названием')

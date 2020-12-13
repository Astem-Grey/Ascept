
from abc import ABC
class Data(ABC):

    daym = []

    def __init__(self, dayma):
        self.dayma = dayma
        Data.daym = self.get_daym2()


    def get_daym2(self):
        self.dayma = self.dayma.split('-')
        self.dayma = list(map(int, self.dayma))
        ss = self.dayma
        return self.dayma


    @classmethod
    def get_data(cls):
        # self.daym = self.daym.split('-')
        # self.daym.map(int)
        # print('.'.join(self.daym))
        return cls.daym

    @staticmethod
    def check_data(date):
        if date[1] > 12:
            print("Неправильная месяц")
        elif date[0] > 31:
            print('Неправильный день')
        else:
            print('Все норма')


dta = Data('25-12-2145')
print(Data.get_data())
# dta.get_daym2()
Data.check_data(Data.get_data())
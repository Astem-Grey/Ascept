
class WareHouse:

    def __init__(self):
        self.name_company = 'TypeWriter'
        self.area = 200
        self.busy = 0
        self.qqq = {'P': Printer, 'S': Scanner, 'C': CopyMachine}

    def __call__(self, operation, name, qua):
        self.operation = operation
        if operation == '+':
            self.qqq.get(name).quantity = self.qqq.get(name).quantity + qua
        elif operation == '-':
            self.qqq.get(name).quantity = self.qqq.get(name).quantity - qua
            if self.qqq.get(name).quantity < 0:
                print('Столько на складе нет')

        self.busy = Printer.quantity + CopyMachine.quantity + Scanner.quantity
        return self.busy

    @staticmethod
    def dict_device():
        all_dict = {"Принтер": Printer.quantity, "Сканер": Scanner.quantity, "Копир": CopyMachine.quantity}
        return all_dict


class OrgTech:

    def __init__(self):

        self.color = 'White'
        self.model = 'TypeWriter'



class Printer(OrgTech):
    quantity = 50

    def __init__(self):
        super().__init__()
        self.name = 'Printer'
        self.speed_write = 30
        self.quantity = Printer.quantity


class Scanner(OrgTech):
    quantity = 50

    def __init__(self):
        super().__init__()
        self.name = 'Scanner'
        self.speed_scan = 20
        self.quantity = Scanner.quantity


class CopyMachine(OrgTech):
    quantity = 50

    def __init__(self):
        super().__init__()
        self.name = 'CopyMachine'
        self.speed_scan = 20
        self.speed_write = 30
        self.quantity = CopyMachine.quantity


# Тут, конечно можно что угодно сделать. Но вот я решил обозначить так
print('Погрузка "+" или выгрузка "-"')
print("Принтер - P, Сканер - S, Копир - C")

while True:
    while True:
        inp1 = input('Какой вид работ?(+ или -) : ')
        inp2 = input('Тип устройства на загрузку или выгрузку: ')
        print('Остановиться - просто Enter')
        if (inp1 != '+' and inp1 != '-' and inp1 != '') or (inp2 != 'P' and inp2 != 'S' and inp2 != 'C' and inp2 != ''):
            print('Вы неправльно введи наименование или тип работ')
        else:
            break
    if inp1 == '' or inp2 == '':
        break

    while True:
        try:
            inp3 = int(input('Количество устройст: '))
        except ValueError:
            print("Неправильно ввел данные")
        else:
            break

    inp_end = WareHouse()

    print(f'Всего устройств: {inp_end(inp1, inp2, inp3)}')
    print(WareHouse.dict_device())


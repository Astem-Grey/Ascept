
# У меня, конечно, больше похоже на перехват ошибки, а не на обработку ее

class ErrorZero():

    def __init__(self, b):
        # self.text = text
        self.b = b


    def __truediv__(self, other):
        if other.b == 0:
            return 'Это деление на 0'
        else:
            return self.b / other.b


ch1 = ErrorZero(int(input('Введите первое число для деления: ')))
ch2 = ErrorZero(int(input('Введите второе число для деления: ')))
print(ch1/ch2)


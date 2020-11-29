
numbers = input('Введите некоторые числа через пробел: ').split(' ')
cash = 0
s = 0


def isintorfloat(s):
    """Проверка числа на принадлежность к действительному числу"""
    try:
        s = int(s)
        return s
    except ValueError:
        try:
            s = float(s)
            return s
        except ValueError:
            if s == 'qqq':          #Тебя может забыть Bethesda, но Скайрим ты не забудешь никогда(Извиняюсь что не по делу, но я был фаном Скайрима)
                return s


while True:
    for s in numbers:
        s = isintorfloat(s)
        if s == 'qqq':
            break
        elif s is None:
            break
        cash = cash + s
    if s == 'qqq':
        print(f'Сумма всех ваших чисел {cash}')
        break
    elif s is None:
        print('Я так не играю')
        break

    print(f'Сумма всех ваших чисел {cash}')
    numbers = input('Хотите еще числа ввести?(Чтоб остановаться введите qqq через пробел) :').split(' ')

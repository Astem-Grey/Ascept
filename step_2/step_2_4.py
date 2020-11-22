
my_list = input('Введите любое предложение: ').split()
i = 0
for ls in my_list:
    i += 1
    if len(ls) > 10:
        print(f'{i}-я строка {ls[0:10]}')
    else:
        print(f'{i}-я строка {ls}')


print('Давайте посчитаем рентабельность вашей компании')
proceeds = int(input('Введите значение вашей выручки - '))
cost = int(input('Введите объем ваших затрат - '))

if proceeds > cost:
    earnings = proceeds - cost
    rent = earnings / proceeds
    print(f'Прибыль вашей компании {earnings}')
    mans = int(input('Сколько людей в вашей компании?: '))
    ear_mans = earnings / mans
    print(f'Рентабельность вашей прибыли - {rent}')
    print(f'Прибыль на одного человека {ear_mans}')
elif proceeds == cost:
    print('Прибыль вашей компании нулевая')
else:
    print('Ваша компания ушла в минус')

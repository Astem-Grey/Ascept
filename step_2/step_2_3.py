
n = input('Введите месяц целым числом: ')

dict_mount = {'1': 'Зима', '2': 'Зима', '3': 'Весна', '4': 'Весна', '5': 'Весна', '6': 'Лето', '7': 'Лето', '8': 'Лето',
              '9': 'Осень', '10': 'Осень', '11': 'Осень', '12': 'Зима'}

print(f'Данное время года {dict_mount.get(n)}')
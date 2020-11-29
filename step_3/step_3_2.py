
def check_data(date):
    """ Функция для проверки правильности введения даты. Пока не полная"""
    # day1, mount1, year = input('Введте дату в числовом варианте: ').split('.')
    day1, mount1, year = date.split('.')
    year = int(year)

    day = {'01': 'Первое', '02': 'Второе', '03': 'Третье', '04': 'Четвертое', '05': 'Пятое', '06': 'Шестое',
           '07': 'Седьмое', '08': 'Восьмое', '09': 'Девятое', '10': 'Десятое', '11': 'Одинадцатое', '12': 'Двенадцатое',
           '13': 'Тринадцатое', '14': 'Четырнадцатое', '15': 'Пятнадцатое', '16': 'Шестнадцатое', '17': 'Семьнадцатое',
           '18': "Восемьнадцатое", '19': 'Девятнадцатое', '20': 'Двадцатое', '21': 'Двадцать первое',
           '22': 'Двадцать второе', '23': 'Двадцать третье', '24': 'Двадцать четвертое', '25': 'Двадцать пятое',
           '26': 'Двадцать шестое', '27': 'Двадцать седьмое', '28': 'Двадцать восьмое', '29': 'Двадцать девятое',
           '30': 'Тридцатое', '31': 'Тридцать первое'}

    mount = {'01': 'Январь', '02': 'Февраль', '03': 'Март', '04': 'Апрель', '05': 'Май', '06': 'Июнь', '07': 'Июль',
             '08': 'Август', '09': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}
    i = 0
    while i != 1:
        if year % 4 != 0 and mount == '02':
            if 0 < int(day1) <= 28:
                i = 1
                break  # print(f'Дата: {day.get(day1)} {mount.get(mount1)} {year} года')
            else:
                print('Такого дня нет в этома месяце. В феврале 28 дней')
        elif year % 4 == 0 and mount == '02':
            if 0 < int(day1) <= 29:
                i = 1
                break  # print(f'Дата: {day.get(day1)} {mount.get(mount1)} {year} года')
            else:
                print('Это високосный год. В феврале 29 дней')
        elif mount1 == '04' or mount1 == '06' or mount1 == '07' or mount1 == '11':
            if 0 < int(day1) <= 30:
                i = 1
                break  # print(f'Дата: {day.get(day1)} {mount.get(mount1)} {year} года')
            else:
                print('В этом месяце 30 дней')
        elif mount1 == '01' or mount1 == '03' or mount1 == '05' or mount1 == '07' or mount1 == '08' or mount1 == '10'\
                or mount1 == '12':
            if 0 < int(day1) <= 31:
                i = 1
                break  # print(f'Дата: {day.get(day1)} {mount.get(mount1)} {year} года')
            else:
                print('В этом месяце 31 день')
        else:
            # print(f'Дата: {day.get(day1)} {mount.get(mount1)} {year} года')
            print('Больше 31 дня в месяце не бывает, ну и в феврале больше 29 тоже')
        day1, mount1, year = input('Теперь введите правильную дату в числовом варианте: ').split('.')
        year = int(year)
    else:
        return


def func_pers_area():
    dict_all = {}
    list_info = ['Имя', 'Фамилия', 'Год рождения', 'Город проживания', 'email', 'Телефон']
    for ind in list_info:
        dict_time = {ind: input(f'Введите ваши данные {ind}: ')}
        if ind == 'Год рождения':
            check_data(dict_time.get(ind))
        dict_all.update(dict_time)
    return dict_all


dict_man = func_pers_area()
y = dict_man.values()
print(f'{dict_man.get("Имя")} {dict_man.get("Фамилия")} родился {dict_man.get("Год рождения")} проживает в городе '
      f'{dict_man.get("Город проживания")}. Email: {dict_man.get("email")}. Телефон: {dict_man.get("Телефон")}')
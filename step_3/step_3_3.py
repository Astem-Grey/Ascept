
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
            return False


def summ_max(one, two, thr):
    list_num = [one, two, thr]
    max_1 = max(list_num)
    list_num.remove(max_1)
    max_2 = max(list_num)
    return max_1 + max_2


num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')
num3 = input('Введите третьте число. Сча мы найдем их них два максимальных и сложим: ')

num1 = isintorfloat(num1)
num2 = isintorfloat(num2)
num3 = isintorfloat(num3)

if num1 is False or num2 is False or num3 is False:
    print('Одно из трех вообще не число')
    # Я извиняюсь за такие сокращения, но знаю как сделать чтоб возвращалась и снова спрашивала число
    # Или показывала какой именно пункт неправильный
else:
    print(f'Сумма двух максимальны чисел - {summ_max(num1, num2, num3)}')

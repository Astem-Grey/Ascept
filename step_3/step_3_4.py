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


def isint(a):
    """Проверка, что число целое"""
    try:
        a = int(a)
        return a
    except ValueError:
        return False


def stepen(x, y):
    """Возведение в степень двух чисел"""
    z = x ** y
    return z


num1 = input('Введите  положительное действительное число: ')
num2 = input('Введите отрицательное целое число: ')

while isintorfloat(num1) is False or isintorfloat(num1) < 0:
    num1 = input('Введите всетаки положительное действительное число: ')
else:
    num1 = isintorfloat(num1)

while isint(num2) is False or isint(num2) > 0:
    num2 = input('Введите всетаки отрицательное целое число:')
else:
    num2 = isint(num2)

print(f'Ваши числа возведены в степень: {stepen(num1, num2)}')


class CharCheck(Exception):

    def __init__(self, text):
        self.text = text


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


print('Остановиться - stop')
char_lis = []
while True:
    try:
        chary = input('Введите элемент списка: ')
        if chary == 'stop':
            break
        chary = isintorfloat(chary)
        if chary is False:
            raise CharCheck('Это явно не число')
    except CharCheck as txt:
        print(txt)
    else:
        char_lis.append(chary)

print(char_lis)

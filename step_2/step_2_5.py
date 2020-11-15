
rating = [5, 12, 58, 3, 7, 10]
char = 0

while type(char) == int:

    try:
        char = input('Введите любое натуральное число для добавления в рейтинг: ')

        if char == 'stop':
            print(rating)
            break
        else:
            char = int(char)
    except ValueError:
        print('Это не натуральное число! Введите число:')
        continue

    if rating.count(char) > 0:
        ind = rating.index(char) + rating.count(char)
        rating.insert(ind, char)
    else:
        rating.append(char)
    print(rating)
    print('Остановиться? Напишите - stop')


# Попытался сделать проверку самого введенного массива на повторения, но пока не получилось.
# Но я активно размышляю

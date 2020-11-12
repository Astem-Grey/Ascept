
number = int(input('Введите любое число: '))

stage = 0
number_copy = number
arr = []

if number // 10 == 0:
    print(f'Цыфра {number} самая большая')
else:
    while arr != '':
        if number // 10 != 0:
            arr.append(number % 10)
            number = number // 10
            stage += 1

        else:
            break

    arr.append(number_copy // (10 ** stage))

maximum = arr[0]
for step in range(len(arr)):
    if maximum < arr[step]:
        maximum = arr[step]
    step += 1
print(f' Самая большая цыфра из числа: {maximum}')

# Наверно самое интересное задание.
# Под конец догадался, как сделать одним циклом. Но уж как сделал


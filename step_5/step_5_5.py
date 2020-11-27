from functools import reduce

with open('step_5_5.txt', 'w') as file:
    file.write('25,58,96,14,26,85,47,36,45,25,14,96,36,256')

with open('step_5_5.txt', 'r') as file:
    numbers = file.read().split(',')
    summa = reduce(lambda x, y: int(x) + int(y), numbers)

print(summa)
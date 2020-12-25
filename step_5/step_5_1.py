
file = open('step_5_1.txt', 'w')


while True:
    data = input('Записываю: ')
    wr = file.write(data + '\n')
    if data == '':
        break

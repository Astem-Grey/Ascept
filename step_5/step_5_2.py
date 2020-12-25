
file = open('step_5_2.txt', 'r')
st = 0
list_1 = []

while True:

    file_line = file.readline()
    print(file_line)
    words = file_line.split(' ')
    list_1.append(words)

    if file_line == '':
        break
    else:
        st += 1


print(f'Количество строк - {st}')
for b in list_1:
    if b != ['\n'] and b != ['']:
        print(f'В {list_1.index(b) + 1}-й строке {len(b)} слов')

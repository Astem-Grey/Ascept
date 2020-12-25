
dict_sotr = {}
sredn = 0

with open('step_5_3.txt', 'r', encoding='Utf-8') as file:
    while True:
        text = file.readline().split(' : ')
        # print(text)
        if text == ['']:
            break
        try:
            dict_sotr[text[0]] = text[1].replace('\n', '')
        except IndexError:
            continue
print(dict_sotr)

for key in dict_sotr:
    sredn = sredn + int(dict_sotr.get(key))
    if int(dict_sotr.get(key)) < 20000:
        print(f'{key} - получает меньше 20т')

print(f'Средняя зарплата всех сотрудников: {sredn / len(dict_sotr)}')


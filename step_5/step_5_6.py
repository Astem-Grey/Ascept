import re
dict_it = {}
info = ["Информатика", 'Физика', "Физкультура"]
a = 0

with open('step_5_6.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    for st in info:

        perm = re.findall(st + r':.+', text)
        perm2 = re.findall(r'\d+', perm[0])

        for st2 in perm2:
            a = a + int(st2)
        dict_it[st] = a

# То что, я сделал извращенство конечно, но цель задания я выполнил:)
# Я извиняюсь, и опнимаю что при помощи функции json, это было бы проще. Но пока я не могу заставить ее работать(


print(dict_it)
# print(text)

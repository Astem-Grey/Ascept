dict_word = {'One': 'Один', "Two": "Два", "Three": "Три", "Four": "Четыре"}
list_1 = []
with open('step_5_4.txt', 'r', encoding='Utf-8') as file:

    for text in file.readlines():
        print(text)
        text2 = text.split(' ')
        words = dict_word.get(text2[0])
        list_1.append(f'{words} {text2[1]} {text2[2]}')

with open('step_5_4_w.txt', 'w', encoding='Utf-8') as file:
    for i in list_1:
        file.writelines(i)

list_firm = []
list_firm_all = []
dict_firm = {}
all_profit = 0

with open('step_5_7.txt', 'r', encoding='utf-8') as file:
    while True:
        line_firm = file.readline()
        list_firm = line_firm.split(' ')
        try:
            profit = int(list_firm[2]) - int(list_firm[3])
        except IndexError:
            break
        if profit >= 0:
            dict_firm[list_firm[0]] = profit
            all_profit = all_profit + profit

        # profit = int(list_firm[2]) - int(list_firm[3])
        if line_firm == '':
            break

all_profit = int(all_profit / len(dict_firm))
dict_all = {'average_profit': all_profit}
list_all = [dict_firm, dict_all]
print(list_all)

# Чисто позиционный расчет. Но еслиб знаков было больше наверно сделал бы через регулярки

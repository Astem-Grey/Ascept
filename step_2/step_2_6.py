
list_new = []
list_name = []
list_price = []
list_qua = []
list_num = []
list_product_tuple = []
i = int(input('Сколько товаров хотите добавить? '))
f = 0

for a in range(i):

    try:

        name = input('Введите название товара: ')
        price = float(input('Введите цену этого товара: '))
        qua = int(input('Введите количество товара: '))
        num = int(input('Единицы? '))

    except ValueError:
        print('Это не число. Нужно было правильно вводить')
        break

    dict_product = {'Название': name, 'Цена': price, 'Количество': qua, 'Единиц': num}
    list_new.append(dict_product)
    typ = (a + 1, list_new[a])
    list_product_tuple.append(typ)
#    print(typ)

    list_name.append(dict_product.get('Название'))
    list_price.append(dict_product.get('Цена'))
    list_qua.append(dict_product.get('Количество'))
    list_num.append(dict_product.get('Единиц'))

dict_product_all = {'Название': list_name, 'Цена': list_price, 'Количество': list_qua, 'Единиц': list_num}
a = len(list_product_tuple)

for s in range(a):
    print(list_product_tuple[f])
    f += 1

for item in dict_product_all.items():
    print(item)

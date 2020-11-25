
list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_2 = [list_1[el] for el in range(0, len(list_1)) if list_1[el] > list_1[el - 1]]
print(list_2)
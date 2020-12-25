
list_primer = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 5, 12, 12, 589, 56, 56]

list_my = [a for a in list_primer if list_primer.count(a) == 1]
print(list_my)
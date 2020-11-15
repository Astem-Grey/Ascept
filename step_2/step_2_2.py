
list_start = [1, 2, 5, 6, 7, 10, 11, 20]
i = -1

for n in list_start:
    if list_start.index(n) % 2 > 0:
        ind = list_start.index(n)
        list_start.pop(ind)
        list_start.insert(ind - 1, n)

print(list_start)

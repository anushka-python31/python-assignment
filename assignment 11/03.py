#wap to Sort according to the Second Element in Sublist

lst = [[1, 3], [2, 2], [3, 1]]
for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if lst[j][1] > lst[j + 1][1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("Sorted by Second Element:", lst)
#wap to Sort a List according to the Length of the Elements

lst = ["apple", "kiwi", "banana", "fig"]
for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if len(lst[j]) > len(lst[j + 1]):
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("Sorted by Length:", lst)#
#wap to Reverse the list

lst = [1, 2, 3, 4, 5]
reversed_lst = []
for i in range(len(lst)-1, -1, -1):
    reversed_lst.append(lst[i])
print("Reversed List:", reversed_lst)
#wap to find Maximum and Minimum element in a list

lst = [3, 7, 2, 9, 4]
max_val = lst[0]
min_val = lst[0]
for num in lst:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print("Max:", max_val)
print("Min:", min_val)#wap 
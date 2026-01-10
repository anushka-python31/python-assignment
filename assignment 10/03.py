#wap to find the Second largest element in the list

lst = [10, 20, 4, 45, 99]
first = second = float('-inf')
for num in lst:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second Largest:", second)
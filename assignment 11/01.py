#wap to Put Even and Odd elements of a list into two different lists

lst = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even:", even)
print("Odd:", odd)
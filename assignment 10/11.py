#wap to print all numbers which are divisible by m and n in the list
lst = [12, 18, 24, 30, 36]
m = 3
n = 6
for num in lst:
    if num % m == 0 and num % n == 0:
        print(num)
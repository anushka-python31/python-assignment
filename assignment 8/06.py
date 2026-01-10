#wap to find sum of digits of number using function.

def sum_of_digits(num):
    total=0
    while num>0:
        digit =num%10
        total+=digit
        num//=10
    return total
n=int(input("Enter a number:"))
result=sum_of_digits(n)
print("sum of digits is:",result)    
#wap to check if a given number is armstrong or not.for each task create separate function
def count_digits(num):
    return len(str(num))
def armstrong_sum(num,digits):
    total=0
    temp=num
    while temp>0:
        digit=temp%10
        total+=digit**digits
        temp//=10
    return total
def is_armstrong(num):
    digits=count_digits(num)
    return num==armstrong_sum(num,digits)
n=int(input("enter a number:"))
if is_armstrong(n):
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")        
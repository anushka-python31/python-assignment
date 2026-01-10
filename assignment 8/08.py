#wap to check if entered number is palindrom or not using function.

def is_palindrome(num):
    original=num
    reverse=0

    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num//=10

    if original==reverse:
        return True
    else:
        return False
n=int(input("Enter a number:"))
if is_palindrome(n):
    print("the number is a palindrome")
else:
    print("the number is not a palindrom")            
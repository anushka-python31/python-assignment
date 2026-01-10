#wap to find print the following fibonnaci series using functions:
#1 1 2 3 5 8

def fibonacci(num):
    a,b=1,1
    for i in range(num):
        print(a,end=" ")
        a,b=b,a+b
num=6 #number of terms
fibonacci(num)
#wap to find reverse of number using function.

def revnum(num,rev=0):
    if(num==0):
        return rev
    else:
        return revnum(num//10,rev*10+num%10)
    
num=368
rev_num=revnum(num)    
print(rev_num)
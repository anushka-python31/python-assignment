#wap to print list after removing even number
lst = [1, 2, 3, 4, 5, 6] 
odd_lst = []
for num in lst:
     if num % 2 != 0:
         odd_lst.append(num) 
print("List without even numbers:", odd_lst)
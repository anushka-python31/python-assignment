#wap to remove all occurrences of a given element in the list.
lst = [1, 2, 3, 2, 4, 2]
element = int(input("Enter element to remove: ")) 
new_lst = []
for item in lst: 
    if item != element: 
     new_lst.append(item) 
print("Updated List:", new_lst)
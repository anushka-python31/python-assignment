#wap to create a new list from existing list which container Cube of each number of a list

lst = [1, 2, 3, 4]
cube_lst = []
for num in lst:
    cube_lst.append(num * num * num)
print("Cubes:", cube_lst)
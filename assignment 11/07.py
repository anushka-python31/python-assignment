#wap to find the Intersection of Two Lists

a = [1, 2, 3]
b = [3, 4, 5]
intersection = []
for item in a:
    for item2 in b:
        if item == item2 and item not in intersection:
            intersection.append(item)
print("Intersection:", intersection)
#wap to find Union of Two Lists

a = [1, 2, 3]
b = [3, 4, 5]
union = []
for item in a:
    if item not in union:
        union.append(item)
for item in b:
    if item not in union:
        union.append(item)
print("Union:", union)
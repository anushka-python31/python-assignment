s1 = "apple"
s2 = "banana"

def length(s):
    count = 0
    for _ in s:
        count += 1
    return count

print(s1 if length(s1) > length(s2) else s2)  # banana

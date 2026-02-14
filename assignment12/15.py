def string_length(s):
    count = 0
    for _ in s:   # manually count characters
        count += 1
    return count

s1 = "apple"
s2 = "banana"

if string_length(s1) > string_length(s2):
    print("Larger string:", s1)
elif string_length(s2) > string_length(s1):
    print("Larger string:", s2)
else:
    print("Both strings are equal in length")

# accept a number from user and Check if this element is present in the list or not.also tell how many times it is present in the list

lst=[1, 2, 3, 2, 4, 2]
num = int(input("Enter number: "))
count = 0
for item in lst:
    if item == num:
        count += 1
if count > 0:
    print(f"{num} is present {count} times.")
else:
    print(f"{num} is not present.")
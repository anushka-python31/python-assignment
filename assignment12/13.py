s = "Python123"
digits = sum(ch.isdigit() for ch in s)
letters = sum(ch.isalpha() for ch in s)
print("Digits:", digits, "Letters:", letters)

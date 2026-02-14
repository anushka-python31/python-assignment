strings = ["flower", "flow", "flight"]
prefix = ""
for i in range(len(min(strings, key=len))):
    chars = {s[i] for s in strings}
    if len(chars) == 1:
        prefix += chars.pop()
    else:
        break
print(prefix)  # fl

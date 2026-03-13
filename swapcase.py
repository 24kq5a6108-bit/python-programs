a = input()
b = ""
for i in a:
    if i.islower():
        b += i.upper()
    elif i.isupper():
        b += i.lower()
    else:
        b += i
print(b)

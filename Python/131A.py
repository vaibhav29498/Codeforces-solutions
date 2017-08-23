a = input()
if a == a.upper():
    print(a.lower())
elif a[1:] == a[1:].upper():
    print(a.capitalize())
else:
    print(a)
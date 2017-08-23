a = input()
c = 0
for i in range(26):
    if chr(97 + i) in a:
        c += 1
if c % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
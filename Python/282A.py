x = 0
t = int(input())
for i in range(t):
    if '++' in input():
        x += 1
    else:
        x -= 1
print(x)
import math

n = int(input())
a = sorted(list(map(int, input().split())))
c, v, t, o = 0, 0, 0, 0
for i in a:
    if i == 4:
        c += 1
    elif i == 3:
        c += 1
        v += 1
    elif i ==2:
        t += 1
    else:
        o += 1
o -= v + 2 * (t % 2)
if o < 0:
    o = 0
print(c + int(math.ceil(t / 2)) + int(math.ceil(o / 4)))
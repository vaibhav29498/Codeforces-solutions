def abbr(inp):
    l = len(inp)
    if l <= 10:
        return inp
    return inp[0] + str(l - 2) + inp[l - 1]

t = int(input())
for i in range(t):
    print(abbr(input()))
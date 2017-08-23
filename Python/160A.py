n = int(input())
a = list(map(int, input().split()))
s = sum(a) / 2
s2 = 0
a.sort(reverse = True)
for i in range(n):
    s2 += a[i]
    if s2 > s:
        print(i + 1)
        break
n = int(input())
a = list(map(int, input().split()))
c = m = 1
for i in range(1, n):
    if a[i] >= a[i - 1]:
        c += 1
    else:
        if c > m:
            m = c
        c = 1
print(max(c, m))

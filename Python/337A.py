n, m = map(int, input().split())
f = list(map(int, input().split()))
f.sort()
c = 997
for i in range(0,m - n + 1):
    if f[i + n - 1] - f[i] < c:
        c = f[i + n - 1] - f[i]
print(c)
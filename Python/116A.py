n = int(input())
c = m = 0
for i in range(n):
    a, b = map(int, input().split())
    c += b - a
    if c > m:
        m = c
print(m)
n = int(input())
a = list(map(int, input().split()))
c = a.index(max(a)) + a[::-1].index(min(a))
if a.index(max(a)) > n - 1 - a[::-1].index(min(a)):
    c -= 1
print(c)
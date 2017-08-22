n, k = map(int, input().split())
a = list(map(int, input().split()))
if a[k - 1] > 0:
    key = a[k - 1]
    while k < n and a[k] == key:
        k += 1
else:
    while k > 0 and a[k - 1] <= 0:
        k -= 1
print(k)
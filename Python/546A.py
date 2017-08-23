k, n, w = map(int, input().split())
m = k * int((w * (w + 1)) / 2) - n
print(m if m > 0 else 0)
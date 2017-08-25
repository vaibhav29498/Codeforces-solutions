k, l, m, n, d = int(input()), int(input()), int(input()), int(input()), int(input())
a = [0] * d
for i in [k, l, m, n]:
    a[i - 1::i] = [1] * len(a[i - 1::i])
print(sum(a))
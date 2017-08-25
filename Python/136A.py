n = int(input())
a = list(map(int, input().split()))
print(' '.join([str(a.index(i + 1) + 1) for i, x in enumerate(a)]))
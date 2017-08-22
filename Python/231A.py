c = 0
t = int(input())
for i in range(t):
    if sum(list(map(int, input().split()))) > 1:
        c += 1
print(c)
a = []
found = False
for i in range(5):
    a.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            print(abs(2 - i) + abs(2 - j))
            found = True
            break
    if found:
        break
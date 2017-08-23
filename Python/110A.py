a = input()
c = len(list(filter(lambda x: x == '4' or x == '7', a)))
print("YES" if c == 4 or  c == 7 else "NO")
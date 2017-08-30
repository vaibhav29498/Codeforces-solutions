n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = a[1:]
b = b[1:]
if len(list(filter(lambda x:x not in a and x not in b, list(range(1,n+1))))) == 0:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
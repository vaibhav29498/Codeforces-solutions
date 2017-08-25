def distinct(n):
    a = [0] * 10
    while n != 0:
        t = n % 10
        n = int(n / 10)
        a[t] += 1
        if a[t] > 1:
            return False
    return True

def nextYear(n):
    i = n + 1
    while not distinct(i):
        i += 1
    return i

print(nextYear(int(input())))
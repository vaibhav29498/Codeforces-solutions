import math

def divbylucky(n):
    nonlucky = ['0', '1', '2', '3', '5', '6', '8', '9']
    for i in range(2,int(n / 2) + 1):
        if n % i == 0:
            lucky = True
            for elem in nonlucky:
                if elem in str(i):
                    lucky=False
                    break
            if lucky
                return True
    lucky = True
    nonlucky = ['0', '1', '2', '3', '5', '6', '8', '9']
    for elem in nonlucky:
        if elem in str(n):
            lucky = False
            break
    return lucky

print("YES" if divbylucky(int(input())) else "NO")
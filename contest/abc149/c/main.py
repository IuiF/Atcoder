import math

x = int(input())


def prime_check(n):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


while True:
    if prime_check(x) == True:
        break
    else:
        x += 1

print(x)

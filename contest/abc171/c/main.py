n = int(input())
name = ""

while n > 0:
    r = n % 26
    if r == 0:
        name += "z"
        n -= 1
    else:
        name += chr(ord("a") + r - 1)
    n //= 26

print(name[::-1])

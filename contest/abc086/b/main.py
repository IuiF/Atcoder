a, b = input().split()
c = int(a + b)
if int(c ** (1 / 2)) == c ** (1 / 2):
    print("Yes")
else:
    print("No")

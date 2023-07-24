Y = int(input())
if Y % 4 == 2:
    print(Y)
elif Y % 4 == 3:
    print(Y + 3)
elif Y % 4 == 0:
    print(Y + 2)
else:
    print(Y + 1)

x = list(map(int, input().split()))
x.sort()
if x[0] + 3 > x[1]:
    print("Yes")
else:
    print("No")

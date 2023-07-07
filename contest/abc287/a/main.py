N = int(input())
a = [0, 0]
for i in range(N):
    if input() == "For":
        a[0] += 1
    else:
        a[1] += 1
if a[0] > a[1]:
    print("Yes")
else:
    print("No")

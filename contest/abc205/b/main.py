n = int(input())
a = list(map(int, input().split()))
a.sort()
b = list(i for i in range(1, n + 1))
if a == b:
    print("Yes")
else:
    print("No")

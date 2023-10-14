n = int(input())
a = list(map(int, input().split()))
if all(a[0] == i for i in a):
    print("Yes")
else:
    print("No")

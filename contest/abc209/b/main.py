n, x = map(int, input().split())
a = list(map(int, input().split()))
if x >= (sum(a) - len(a) // 2):
    print("Yes")
else:
    print("No")

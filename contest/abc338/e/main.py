n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

if any(abs(a[i][0] - a[i][1]) % 2 == 0 for i in range(n)):
    print("Yes")
else:
    print("No")

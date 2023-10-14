def check(N):
    while N % 2 == 0:
        N //= 2
    while N % 3 == 0:
        N //= 3
    return N == 1


n = int(input())
if check(n):
    print("Yes")
else:
    print("No")

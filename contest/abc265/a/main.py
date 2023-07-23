X, Y, N = map(int, input().split())
if X * 3 > Y:
    ans = N // 3 * Y + N % 3 * X
    print(ans)
else:
    print(N * X)

N, M, X, T, D = map(int, input().split())
if X <= M <= N:
    print(T)
elif M < X:
    print(T - (X - M) * D)
else:
    print(T + (N - M) * D)

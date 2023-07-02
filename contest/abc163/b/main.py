N, M = map(int, input().split())
num = sum(map(int, input().split()))
print(-1 if N - num < 0 else N - num)

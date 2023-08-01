N, K, A = map(int, input().split())
t = (K + A - 1) % N

print(t if t != 0 else N)

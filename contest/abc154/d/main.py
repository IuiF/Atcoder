N, K = map(int, input().split())
P = list(map(int, input().split()))

Exp = [0]

for i in range(1, 1001):
    Exp.append((1 + i) / 2)

P_arr = [0 for _ in range(N + 1)]
for i in range(N):
    P_arr[i + 1] = P_arr[i] + Exp[P[i]]

ans = 0
for i in range(K, N + 1):
    ans = max(ans, P_arr[i] - P_arr[i - K])

print(ans)

N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())[::-1]
P = list(map(int, input().split()))[::-1]

ans = 0

for i in range(N):
    tmp = 0
    for j in range(M):
        if C[i] == D[j]:
            ans += P[j]
        else:
            tmp += 1
    if tmp == M:
        ans += P[-1]

print(ans)

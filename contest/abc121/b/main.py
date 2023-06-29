N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    total_tmp = 0
    for j in range(M):
        total_tmp += tmp[j] * B[j]
    total_tmp += C
    if total_tmp > 0:
        ans += 1

print(ans)

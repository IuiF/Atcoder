N = int(input())
L = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if (
                sum([L[i], L[j], L[k]]) > 2 * max([L[i], L[j], L[k]])
                and L[i] != L[j]
                and L[i] != L[k]
                and L[j] != L[k]
            ):
                ans += 1

print(ans)

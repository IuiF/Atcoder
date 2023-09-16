M = int(input())
S = [list(input()) for _ in range(3)]
S_st = [set(S[i]) for i in range(3)]
common = S_st[0].intersection(S_st[1]).intersection(S_st[2])

ans = 0

if len(common) == 0:
    ans = -1
else:
    ans = float("inf")
    for num in common:
        for i in range(M):
            for j in range(M):
                for k in range(M):
                    if S[0][i] == S[1][j] == S[2][k] == num:
                        if i == j == k:
                            t = i + M * 2
                        elif i == j or i == k:
                            t = i + M
                        elif j == k:
                            t = j + M
                        else:
                            t = max(i, j, k)
                        ans = min(ans, t)


print(ans)

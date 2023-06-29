N = int(input())
S = list(input())
ans = 0
for i in range(1, N):
    set_x = set(S[:i])
    set_y = set(S[i:])

    ans = max(ans, (len(set_x & set_y)))

print(ans)

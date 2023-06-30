S = list(input().rstrip())
T = list(input().rstrip())
ans = 0
for i in range(len(S)):
    if S[i] == T[i]:
        ans += 1

print(ans)

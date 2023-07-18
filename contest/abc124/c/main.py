S = list(input())
ans = 0

for i in range(1, len(S)):
    if int(S[i - 1]) == int(S[i]):
        S[i] = not int(S[i])
        ans += 1


print(ans)

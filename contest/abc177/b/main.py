S = input()
T = input()
ans = 1000

for i in range(len(S)):
    tmp = 0
    try:
        for j in range(len(T)):
            if S[i + j] == T[j]:
                continue
            else:
                tmp += 1
                continue
    except IndexError:
        tmp = 1000
    ans = min(ans, tmp)
print(ans)

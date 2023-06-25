S = list(input())

for _ in range(len(S) // 2):
    if len(S) % 2 == 0:
        S.pop(-1)
        S.pop(-1)
    else:
        S.pop(-1)

    if S[len(S) // 2 :] == S[: len(S) // 2]:
        break
print(len(S))

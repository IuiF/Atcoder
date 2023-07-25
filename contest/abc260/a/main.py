S = list(input())
S.sort()
if len(set(S)) == 1:
    print(-1)
elif S[0] == S[1]:
    print(S[2])
else:
    print(S[0])

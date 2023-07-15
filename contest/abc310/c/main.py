N = int(input())
S = set()

for _ in range(N):
    tmp = input()
    if (tmp in S) or (tmp[::-1] in S):
        continue
    else:
        S.add(tmp)

print(len(S))

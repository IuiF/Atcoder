N = int(input())
S = input()
lst = [S[0]]


for i in range(1, N):
    if S[i] == lst[-1]:
        continue
    else:
        lst.append(S[i])

print(len(lst))

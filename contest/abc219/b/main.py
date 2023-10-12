S = [input() for _ in range(3)]
T = input()
ans = []
for i in range(len(T)):
    ans.append(S[int(T[i]) - 1])
print("".join(ans))

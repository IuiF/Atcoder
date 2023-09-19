S = list(input())
A = 0
for i in range(len(S)):
    A += int(S[i])
print("Yes" if A % 9 == 0 else "No")

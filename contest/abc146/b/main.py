num = int(input())
S = list(input())

for i in range(len(S)):
    S[i] = ord(S[i]) + num
    if S[i] > 90:
        S[i] -= 26
    S[i] = chr(S[i])


print(*S, sep="")

S = input().rstrip()
lst = []

i = 0
while i < len(S):
    j = i + 1
    while j < len(S) and S[i] == S[j]:
        j += 1

    lst.append(S[i] + str(j - i))

    i = j

print(*lst, sep="")

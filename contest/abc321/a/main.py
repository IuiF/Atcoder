S = list(input())
for i in range(1, len(S)):
    if int(S[i - 1]) > int(S[i]):
        continue
    else:
        print("No")
        exit()
print("Yes")

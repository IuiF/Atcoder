S = input()
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] in ["R", "U", "D"]:
            continue
        else:
            print("No")
            exit()
    else:
        if S[i] in ["L", "U", "D"]:
            continue
        else:
            print("No")
            exit()
print("Yes")

S = list(input())
ls = [[7], [4], [2, 8], [1, 5], [3, 9], [6], [10]]
f = False


for i in range(1, 11):
    if S[i - 1] == "0":
        for j in range(7):
            if i in ls[j]:
                ls[j].remove(i)
if S[0] == "0":
    for i in range(7):
        if len(ls[i]) > 0:
            for j in range(i + 1, 7):
                if len(ls[j]) == 0:
                    for k in range(j + 1, 7):
                        if len(ls[k]) > 0:
                            f = True


print("Yes" if f else "No")

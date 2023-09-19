S = input()
L = len(S)
if (
    S == S[::-1]
    and S[: L // 2] == S[: L // 2][::-1]
    and S[L // 2 + 1 :] == S[L // 2 + 1 :][::-1]
):
    print("Yes")
else:
    print("No")

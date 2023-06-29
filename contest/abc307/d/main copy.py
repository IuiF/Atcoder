def del_Parentheses(S):
    tmp = []
    i = 0
    while i < len(S):
        if S[i] == "(":
            tmp.append(i)
            i += 1
        elif S[i] == ")" and len(tmp) > 0:
            try:
                S = S[: tmp[-1]] + S[i + 1 :]
                tmp = []
                try:
                    i = tmp[-1]
                except IndexError:
                    i = 0
                continue
            except IndexError:
                S = S[: tmp[-1]]
                tmp = []
                return S
        else:
            i += 1
    if S == "":
        return ""
    return S


N = int(input())
S = input()

print(del_Parentheses(S))

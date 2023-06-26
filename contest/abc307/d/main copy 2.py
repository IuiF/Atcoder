import sys

sys.setrecursionlimit(1000000)


def dfs(S, start, depth):
    res = ""
    i = start
    while i < len(S):
        if S[i] == "(":
            sub_res, i = dfs(S, i + 1, depth + 1)
            if depth > 0:
                res += "(" + sub_res
            else:
                res += sub_res
        elif S[i] == ")":
            if depth > 0:
                return res + ")", i
            else:
                res += S[i]
        else:
            res += S[i]
        i += 1
    return res, i


N = int(input())
S = input()

print(dfs(S, 0, 0)[0])

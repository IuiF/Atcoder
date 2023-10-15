n = int(input())
s = list(input())
ans = []
pos = []
for i in range(n):
    if s[i] == "(":
        pos.append(len(ans))
        ans.append(s[i])
    elif s[i] != ")":
        ans.append(s[i])
    else:
        if len(pos) == 0:
            ans.append(s[i])
        else:
            for _ in range(len(ans) - pos.pop()):
                ans.pop()

print("".join(ans))

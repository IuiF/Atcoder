s = list(input())
ans = []
t = [0]


for i in range(len(s)):
    if s[i] == "A":
        ans.append(s[i])
        t.append(1)
    elif s[i] == "B":
        ans.append(s[i])
        if t[-1] == 1:
            t.append(2)
        else:
            t.append(0)
    elif s[i] == "C":
        ans.append(s[i])
        if t[-1] == 2:
            t.pop()
            t.pop()
            ans.pop()
            ans.pop()
            ans.pop()
        else:
            t.append(0)

print(*ans, sep="")

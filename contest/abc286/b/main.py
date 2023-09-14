n = int(input())
s = list(input())
ans = []
for i in range(1, n):
    if s[i - 1] == "n" and s[i] == "a":
        ans.append("ny")
    else:
        ans.append(s[i - 1])
ans.append(s[-1])
print("".join(ans))

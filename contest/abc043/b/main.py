s = input()
ans = []
for i in range(len(s)):
    if s[i] == "B":
        try:
            ans.pop()
        except IndexError:
            continue
    else:
        ans.append(s[i])
print("".join(ans))

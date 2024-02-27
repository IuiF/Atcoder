s = list(input())

ans = [s[0]]
for i in range(1, len(s)):
    if ans[-1] == s[i]:
        continue
    else:
        ans.append(s[i])

if "".join(ans) in ["ABC", "AC", "AB", "BC", "A", "B", "C", ""]:
    print("Yes")
else:
    print("No")

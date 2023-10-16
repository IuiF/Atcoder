s = input()[::-1]
ans = 0
for i in range(len(s)):
    t = int(ord(s[i]) - ord("A") + 1)
    ans += t * 26**i
print(ans)

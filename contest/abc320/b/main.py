s = input()
ans = 1
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i : j + 1] == s[i : j + 1][::-1]:
            ans = max(ans, j - i + 1)
print(ans)

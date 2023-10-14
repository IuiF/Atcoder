n, t = input().split()
n = int(n)
ans = []
for i in range(n):
    s = input()
    if len(s) == len(t):
        if s == t:
            ans.append(i + 1)
        else:
            if sum([s[j] != t[j] for j in range(len(s))]) == 1:
                ans.append(i + 1)
    elif len(s) == len(t) + 1:
        diff = False
        for j in range(len(t)):
            if s[j] != t[j - diff]:
                if diff or s[j + 1 :] != t[j:]:
                    break
                diff = True
        else:
            ans.append(i + 1)
    elif len(s) + 1 == len(t):
        diff = False
        for j in range(len(s)):
            if s[j - diff] != t[j]:
                if diff or s[j:] != t[j + 1 :]:
                    break
                diff = True
        else:
            ans.append(i + 1)

print(len(ans))
print(*ans)

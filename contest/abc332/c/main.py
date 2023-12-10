n, m = map(int, input().split())
s = input()
p = m
t = 0
ans = 0

for i in range(n):
    if s[i] == "1":
        if p > 0:
            p -= 1
        else:
            t += 1
    elif s[i] == "2":
        t += 1
    else:
        ans = max(ans, t)
        t = 0
        p = m

ans = max(ans, t)
print(ans)

s = list(input())
n = len(s) - 1
sa = ""

ans = 0

for i in range(2**n):
    copy_s = s.copy()
    sub = ""
    for j in range(n):
        if (i >> j) & 1:
            sub += copy_s.pop(0) + "+"
        else:
            sub += copy_s.pop(0)
    sub += copy_s.pop(0)
    ans += eval(sub)

print(ans)

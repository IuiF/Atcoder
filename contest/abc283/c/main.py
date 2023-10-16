s = input()
ls = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ans = 0
p = 0
while p < len(s):
    if s[p] in ls:
        ans += 1
        p += 1
    elif s[p] == "0":
        try:
            if s[p + 1] == "0":
                ans += 1
                p += 2
            else:
                ans += 1
                p += 1
        except IndexError:
            ans += 1
            break

print(ans)

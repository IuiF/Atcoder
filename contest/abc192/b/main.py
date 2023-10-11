s = input()
f = True
for i in range(len(s)):
    if i % 2 == 0:
        if s[i].islower():
            continue
        else:
            f = False
            break
    else:
        if not s[i].islower():
            continue
        else:
            f = False
            break
print("Yes" if f else "No")

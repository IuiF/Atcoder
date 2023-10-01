s = input()
t = input()
f = True
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    elif s[i] == "@":
        if t[i] in "atcoder":
            continue
        else:
            f = False
            break
    elif t[i] == "@":
        if s[i] in "atcoder":
            continue
        else:
            f = False
            break
    else:
        f = False
        break
print("You can win" if f else "You will lose")

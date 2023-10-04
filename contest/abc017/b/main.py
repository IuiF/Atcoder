x = input()
f = True
while f:
    if len(x) > 1 and x[:2] == "ch":
        x = x[2:]
    elif len(x) > 0 and x[0] in "oku":
        x = x[1:]
    elif len(x) == 0:
        break
    else:
        f = False
print("YES" if f else "NO")

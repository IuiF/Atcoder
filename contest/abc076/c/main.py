s = input()
t = input()

for i in range(len(s) - len(t), -1, -1):
    flag = True
    for j in range(len(t)):
        if s[i + j] != "?" and s[i + j] != t[j]:
            flag = False
            break
    if flag:
        s = s[:i] + t + s[i + len(t) :]
        s = s.replace("?", "a")
        print(s)
        break
else:
    print("UNRESTORABLE")

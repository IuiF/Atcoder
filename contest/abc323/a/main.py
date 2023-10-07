s = input()
f = True

for i in range(1, len(s), 2):
    if s[i] == "1":
        f = False
        break
print("Yes" if f else "No")

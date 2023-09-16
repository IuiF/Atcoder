s = list(input())
t = list(input())
tmp = []
for i in range(0, 26):
    tmp = []
    for j in range(len(s)):
        a = chr(ord(s[j]) + i)
        if a > "z":
            a = chr(ord(s[j]) + i - 26)
        tmp.append(a)
    if t == tmp:
        print("Yes")
        exit()
print("No")

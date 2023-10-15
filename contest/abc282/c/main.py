n = int(input())
s = list(input())
pos = 0
p = 0
for i in range(len(s)):
    if s[i] == '"':
        if p % 2 == 0:
            p += 1
        else:
            p += 1
    elif s[i] == ",":
        if p % 2 == 0:
            s[i] = "."

print(*s, sep="")

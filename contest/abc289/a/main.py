s = list(input())
for i in range(len(s)):
    s[i] = int(not int(s[i]))
print(*s, sep="")

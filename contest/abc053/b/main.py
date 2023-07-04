s = input()
start = 0
end = 0

for i in range(len(s)):
    if s[i] == "A":
        start = i
        break

for i in range(len(s)):
    if s[-i - 1] == "Z":
        end = i
        break

print(len(s) - (end + start))

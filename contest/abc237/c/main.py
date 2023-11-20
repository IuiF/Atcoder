s = list(input())
start_count = 0
end_count = 0

if len(set(s)) == 1:
    print("Yes")
    exit()

for i in range(len(s)):
    if s[i] == "a":
        start_count += 1
    else:
        break

for i in range(len(s) - 1, -1, -1):
    if s[i] == "a":
        end_count += 1
    else:
        break

if start_count > end_count:
    print("No")
else:
    a = ["a" for _ in range(end_count - start_count)]
    a.extend(s)
    print("Yes" if a == a[::-1] else "No")

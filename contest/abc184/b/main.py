n, p = map(int, input().split())
s = list(input())
for i in s:
    if i == "x" and p > 0:
        p -= 1
    elif i == "o":
        p += 1
print(p)

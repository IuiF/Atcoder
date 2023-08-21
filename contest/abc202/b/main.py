S = list(input())[::-1]
ans = []

for i in S:
    if i == "6":
        ans.append("9")
    elif i == "9":
        ans.append("6")
    else:
        ans.append(i)

print(*ans, sep="")

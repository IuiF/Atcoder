n, k = map(int, input().split())
s = list(input())
ans = []
tmp = 0
for i in s:
    if i == "o" and tmp < k:
        ans.append(i)
        tmp += 1
    else:
        ans.append("x")
print("".join(ans))

n = int(input())
p = list(map(int, input().split()))
q = []
for i in range(n):
    if p[i] == i + 1:
        q.append("x")
    else:
        q.append("o")


ans = 0
for i in range(n):
    if q[i] == "x":
        if i + 1 < n and q[i + 1] == "x":
            q[i] = "o"
            q[i + 1] = "o"
        else:
            q[i] = "o"
        ans += 1

print(ans)

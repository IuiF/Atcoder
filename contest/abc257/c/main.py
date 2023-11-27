n = int(input())
s = input()
w = list(map(int, input().split()))
q = [(w[i], s[i]) for i in range(n)]
q.sort(key=lambda x: (x[0], x[1]))

i = 1
ans = s.count("1")
zeros = 0
ones = ans

for i in range(n):
    if q[i][1] == "0":
        zeros += 1
    else:
        ones -= 1
    if i == n - 1 or q[i][0] != q[i + 1][0]:
        ans = max(ans, ones + zeros)

print(ans)

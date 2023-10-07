n = int(input())
a = []
for _ in range(n):
    s, p = input().split()
    p = int(p)
    a.append((s, p))
a.sort(key=lambda x: x[1], reverse=True)
if a[0][1] >= sum(a[i][1] for i in range(len(a))) // 2 + 1:
    print(a[0][0])
else:
    print("atcoder")

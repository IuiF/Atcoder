N, K = map(int, input().split())
m = []

for _ in range(N):
    a, b = map(int, input().split())
    m.append((a, b))

m.sort(reverse=True)

tmp = 0
for i in range(N):
    tmp += m[i][1]
    if tmp > K:
        print(m[i][0] + 1)
        exit()
    elif i == N - 1:
        print(1)

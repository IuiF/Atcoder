N, K = map(int, input().split())
Ns = list(map(int, input().split()))
Num = [0] * (N + 1)
ans = 0

for i in range(N):
    Num[Ns[i]] += 1

Num.sort(reverse=True)

while Num[-1] != 0:
    if Num[-1] == 0:
        Num.pop()

for _ in range(len(Num) - K):
    ans += Num[-1]
    Num.pop()

print(ans)

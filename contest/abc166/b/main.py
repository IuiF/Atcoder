N, K = map(int, input().split())
ans = set([i for i in range(1, N + 1)])
st = set()

for _ in range(K):
    input()
    tmp = list(map(int, input().split()))
    for i in tmp:
        ans.discard(i)

print(len(ans))

from itertools import combinations


def dfs(pos, selected, t):
    global all_comb, G, max_sum

    if n - sum(selected) in [0, 1]:
        return

    if pos == len(all_comb):
        return 0

    a, b = all_comb[pos]
    if not selected[a] and not selected[b]:
        selected[a] = True
        selected[b] = True
        tmp = G[a][b] + dfs(pos + 1, selected, t)
        t = max(t, tmp)
        max_sum = max(t, tmp)
        selected[a] = False
        selected[b] = False

    max_sum = max(max_sum, dfs(pos + 1, selected, t))
    return max_sum


n = int(input())

G = []
for _ in range(n - 1):
    G.append(list(map(int, input().rstrip().split())))

num = [i for i in range(n)]
all_comb = list(combinations(num, 2))

max_sum = 0
ans = 0

for i in range(len(all_comb)):
    selected = [False for _ in range(n)]
    ans = dfs(i, selected, 0)

print(ans)

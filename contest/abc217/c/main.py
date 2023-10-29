n = int(input())
p = list(map(int, input().split()))
q = [(i + 1, p[i]) for i in range(n)]
q.sort(key=lambda x: x[1])

print(*[i for i, _ in q])

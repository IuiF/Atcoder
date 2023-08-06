n = int(input())
p = list(map(int, input().split()))
print(max(p) - p[0] + 1 if max(p) != p[0] else 1 if p.count(p[0]) > 1 else 0)

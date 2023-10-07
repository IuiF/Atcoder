n = int(input())
s = [input() for _ in range(n)]

ans = [(s[i].count("o"), i + 1) for i in range(n)]
ans.sort(key=lambda x: (-x[0], x[1]))
print(" ".join(str(x[1]) for x in ans))

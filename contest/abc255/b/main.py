n, k = map(int, input().split())
a = list(map(int, input().split()))
lights = []
darks = []
for i in range(n):
    if i + 1 in a:
        lights.append(list(map(int, input().split())))
    else:
        darks.append(list(map(int, input().split())))
ans = []
for i in darks:
    tmp = float("inf")
    for j in lights:
        t = abs(i[0] - j[0]) ** 2 + abs(i[1] - j[1]) ** 2
        tmp = min(tmp, t)
    ans.append(tmp)
print(max(ans) ** (1 / 2))

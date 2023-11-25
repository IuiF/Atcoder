d = int(input())
ans = float("inf")
t = []
for i in range(int(d**0.5) + 2):
    t.append(i**2)

a, b = 0, len(t) - 1
while a <= b:
    current = abs(t[a] + t[b] - d)
    ans = min(ans, current)
    if t[a] + t[b] < d:
        a += 1
    else:
        b -= 1

print(ans)

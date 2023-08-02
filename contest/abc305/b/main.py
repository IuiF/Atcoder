distance = [3, 1, 4, 1, 5, 9, 0]
p, q = input().split()

p = ord(p) - 65
q = ord(q) - 65

if p <= q:
    ans = sum(distance[p:q])
else:
    ans = sum(distance[q:p])

print(ans)

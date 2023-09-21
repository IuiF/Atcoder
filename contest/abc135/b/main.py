n = int(input())
p = list(map(int, input().split()))
tmp = 0
for i in range(n):
    if p[i] != i + 1:
        tmp += 1
print("YES" if (tmp in [0, 2]) else "NO")

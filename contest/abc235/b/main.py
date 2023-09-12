n = int(input())
h = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if h[ans] < h[i] and i - ans == 1:
        ans = i
print(h[ans])

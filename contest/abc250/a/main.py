H, W = map(int, input().split())
R, C = map(int, input().split())
ans = 4
if R + 1 > H:
    ans -= 1
if R - 1 < 1:
    ans -= 1
if C + 1 > W:
    ans -= 1
if C - 1 < 1:
    ans -= 1
print(ans)

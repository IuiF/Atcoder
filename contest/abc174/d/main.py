N = int(input())
C = list(input())
cursor_L = 0
cursor_R = N - 1
ans = 0
while cursor_L < cursor_R:
    while cursor_L < N and C[cursor_L] == "R":
        cursor_L += 1
    while cursor_R >= 0 and C[cursor_R] == "W":
        cursor_R -= 1
    if cursor_L < cursor_R:
        ans += 1
        cursor_L += 1
        cursor_R -= 1

print(ans)

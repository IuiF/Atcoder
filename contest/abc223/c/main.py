n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
half_time = sum(a[i][0] / a[i][1] for i in range(n)) / 2
ans = 0
for i, j in a:
    if i / j > half_time:
        ans += j * half_time
        break
    else:
        half_time -= i / j
        ans += i

print(ans)

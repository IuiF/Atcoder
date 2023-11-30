n, m = map(int, input().split())

if n**2 < m:
    print(-1)
else:
    ans = []
    for i in range(1, int(m**0.5) + 2):
        if m % i == 0:
            a = m // i
        else:
            a = m // i + 1
        if a <= n:
            ans.append(a * i)
    print(min(ans))

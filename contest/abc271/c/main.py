n = int(input())
a = list(map(int, input().split()))

st = set(a)
ans = 0
now = 1


while n > 0:
    if now in st:
        now += 1
        ans += 1
        n -= 1
    else:
        if n >= 2:
            now += 1
            ans += 1
            n -= 2
        else:
            break


print(ans)

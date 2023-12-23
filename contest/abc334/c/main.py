n, k = map(int, input().split())
a = list(map(int, input().split()))
if k % 2 == 0:
    ans = 0
    p = 0
    while p < k - 1:
        ans += a[p + 1] - a[p]
        p += 2
    print(ans)
else:
    if k == 1:
        print(0)
    else:
        p = 0
        tmp = []
        while p < k - 1:
            tmp.append(a[p + 1] - a[p])
            p += 1
        odd_t = [tmp[i] for i in range(len(tmp)) if i % 2 == 1]
        even_t = [tmp[i] for i in range(len(tmp)) if i % 2 == 0]
        ans = sum(odd_t)
        t = sum(odd_t)
        # print(even_t, odd_t)
        for i in range(len(odd_t)):
            t += even_t[i] - odd_t[i]
            ans = min(ans, t)
        print(ans)

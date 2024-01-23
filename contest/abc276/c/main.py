n = int(input())
a = list(map(int, input().split()))
p = [a[-1]]

for i in range(n - 2, -1, -1):
    if p[-1] > a[i]:
        p.append(a[i])
    else:
        for j in range(len(p)):
            if p[j] < a[i]:
                t = p.pop(j)
                p.append(a[i])
                p.sort(reverse=True)
                print(*a[:i], t, *p)
                exit()

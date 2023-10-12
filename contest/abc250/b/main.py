n, a, b = map(int, input().split())
ans = []
for i in range(n):
    for j in range(a):
        tmp = []
        for k in range(n):
            if i % 2 == 0:
                if k % 2 == 0:
                    tmp.append("." * b)
                else:
                    tmp.append("#" * b)
            else:
                if k % 2 == 0:
                    tmp.append("#" * b)
                else:
                    tmp.append("." * b)
        ans.append("".join(tmp))
print("\n".join(ans))

N, D = map(int, input().split())
ls = [list(input()) for _ in range(N)]
check_ls = [0 for _ in range(D)]
ans = 0


for i in range(D):
    Flag = True
    for j in range(N):
        if ls[j][i] == "x":
            Flag = False
            break
    if Flag:
        check_ls[i] = 1

count = 0
for i in check_ls:
    if i == 1:
        count += 1
        ans = max(ans, count)
    else:
        count = 0


print(ans)

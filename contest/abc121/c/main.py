N, M = map(int, input().split())
price_list = [list(map(int, input().split())) for _ in range(N)]
price_list.sort()
ans = 0

for i in range(N):
    if price_list[i][1] <= M:
        M -= price_list[i][1]
        ans += price_list[i][1] * price_list[i][0]
    else:
        ans += M * price_list[i][0]
        M -= M
    if M == 0:
        break


print(ans)

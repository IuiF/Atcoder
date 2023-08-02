A, B, X = map(int, input().split())

buy_max = 10**9 + 1
buy_min = 0
buy_tmp = (buy_min + buy_max) // 2

while buy_max - buy_min > 1:
    if len(str(buy_tmp)) * B + buy_tmp * A <= X:
        buy_min = buy_tmp
    else:
        buy_max = buy_tmp

    # print(buy_min, buy_tmp, buy_max)

    buy_tmp = (buy_min + buy_max) // 2

print(buy_tmp)

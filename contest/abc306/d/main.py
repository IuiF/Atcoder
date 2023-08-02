num = int(input())
X = [0] * (num + 1)
Y = [0] * (num + 1)

for i in range(1, num + 1):
    tmp = list(input().split())
    X[i] = int(tmp[0])
    Y[i] = int(tmp[1])

dp_table = [[0] * 2 for _ in range(num + 1)]  # 腹痛の有無

for i in range(1, num + 1):
    if X[i] == 1:
        dp_table[i][0] = dp_table[i - 1][0]  # 食べない
        dp_table[i][1] = max(
            dp_table[i - 1][1], dp_table[i - 1][0] + Y[i]
        )  # 腹痛+食べない or 非腹痛+食べる
    elif X[i] == 0:
        dp_table[i][0] = max(
            dp_table[i - 1][0], dp_table[i - 1][0] + Y[i], dp_table[i - 1][1] + Y[i]
        )  # 非腹痛+食べない or 非腹痛+食べる or 腹痛+食べる
        dp_table[i][1] = dp_table[i - 1][1]  # 食べない

print(max(dp_table[num]))

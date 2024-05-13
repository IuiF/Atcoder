# 入力処理
n, m, s, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 最短経路
min_time = b[0] + (s - b[-1])

stores = []
store_count = 0
p = 0
for i in a:
    if i < b[0] or i > b[-1]:
        store_count += 1
    else:
        # 店に最も近いステーションをメモ
        closest_tp = min(b, key=lambda x: abs(x - i))
        stores.append((i, closest_tp))

if t - min_time < store_count:  # 最短経路中の店にすべて寄ったらTimeoutしないか
    print(t - min_time, t)
    exit()

# 余剰時間
remaining_time = t - min_time - store_count

# 追加で寄れる店の数
additional_shops = 0


print(stores)

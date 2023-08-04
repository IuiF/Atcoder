coins500 = int(input())
coins100 = int(input())
coins50 = int(input())

target = int(input())

# コイン枚数最小の組み合わせを見つける

coins = []

for i in range(coins500 + 1):
    for j in range(coins100 + 1):
        for k in range(coins50 + 1):
            if i * 500 + j * 100 + k * 50 == target:
                coins.append([i, j, k])
            elif i * 500 + j * 100 + k * 50 > target:
                break

print(len(coins))

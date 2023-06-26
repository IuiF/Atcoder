P = int(input())
coins = [1]
count = 0
for i in range(1, 11):
    coins.append(coins[i - 1] * (i + 1))
while P != 0:
    for i in range(9, -1, -1):
        if P - coins[i] < 0:
            continue
        P -= coins[i]
        count += 1
        break
print(count)

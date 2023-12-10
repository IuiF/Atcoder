from itertools import combinations


def calculate_variance(weights, bags, D):
    total_weights = []
    for bag in bags:
        weight = 0
        for i in range(len(weights)):
            if bag & (1 << i):
                weight += weights[i]
        total_weights.append(weight)

    mean_weight = sum(total_weights) / D
    variance = sum((weight - mean_weight) ** 2 for weight in total_weights) / D
    return variance


n, d = map(int, input().split())
w = list(map(int, input().split()))
ans = float("inf")

for bags in combinations(range(1 << n), d):
    if sum(bags) == (1 << n) - 1:
        var = calculate_variance(w, bags, d)
        ans = min(ans, var)

print(ans)

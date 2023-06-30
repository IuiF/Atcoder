from itertools import combinations


N = int(input())
lst = list(map(int, input().split()))

comb = list(combinations(lst, 2))

print(sum([a * b for a, b in comb]))

K, N = map(int, input().split())
houses = list(map(int, input().split()))
max_dis = 0

for i in range(N - 1):
    max_dis = max(max_dis, abs(houses[i + 1] - houses[i]))

max_dis = max(max_dis, abs(K - houses[N - 1] + houses[0]))

print(K - max_dis)

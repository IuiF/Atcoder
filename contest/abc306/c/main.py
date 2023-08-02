num = int(input())
num_list = list(map(int, input().split()))

count = {}
for i in range(1, num + 1):
    count[i] = 0

ans = []

for i in range(num * 3):
    count[num_list[i]] += 1
    if count[num_list[i]] == 2:
        ans.append(num_list[i])

print(*ans)

num_list = [int(x) for x in input().split()]
ans = 0

for i in range(len(num_list)):
    ans += num_list[i] * (2**i)

print(ans)

from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))

nim_sum = 0
for num in a:
    nim_sum ^= num

if nim_sum == 0:
    if n % 2 == 0:
        print(0)
    else:
        print(max(a) - 1)
else:
    print(-1)

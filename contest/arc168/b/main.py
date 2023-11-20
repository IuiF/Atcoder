from collections import Counter


n = int(input())
a = list(map(int, input().split()))

nim_sum = 0
for num in a:
    nim_sum ^= num

counter = Counter(a)
max_odd_count_val = max(
    (num for num, count in counter.items() if count % 2 != 0), default=0
)

if nim_sum == 0:
    if max_odd_count_val == 0:
        print(0)
    else:
        print(max_odd_count_val - 1)
else:
    print(-1)

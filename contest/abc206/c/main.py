import collections


N = int(input())
Num = list(map(int, input().split()))
Num_d = collections.Counter(Num)
ans = 0

for i in Num:
    ans += N - Num_d[i]
    Num_d[i] -= 1
    N -= 1

print(ans)

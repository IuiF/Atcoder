import collections


N = int(input())
Num = map(int, input().split())
mod_num = []
ans = 0


for i in Num:
    tmp = i % 200
    mod_num.append(tmp)

mod_num = collections.Counter(mod_num)

for k, v in mod_num.items():
    ans += (v) * (v - 1) // 2

print(ans)

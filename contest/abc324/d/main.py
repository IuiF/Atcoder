import math


N = int(input())
s = list(input())
mini = sorted(s)
mini_num = int("".join(mini))
maxi = sorted(s, reverse=True)
maxi_num = int("".join(maxi))
ans = set()


for i in range(int(math.sqrt(mini_num)), int(math.sqrt(maxi_num)) + 1):
    tmp_i = list(str(i**2).rjust(N, "0"))
    tmp_i.sort()
    if mini == tmp_i:
        ans.add(i)


print(len(ans))

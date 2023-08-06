N = int(input())
A = list(map(int, input().split()))
A_ave = sum(A) / N
ans = 0
for i in A:
    ans += abs(i - A_ave)
ans //= 2
print(int(ans))

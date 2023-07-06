from math import gcd


N = int(input())
A = list(map(int, input().split()))

if N == 2:
    print(max(A))
    exit()

f_gcd = [gcd(A[0], A[1])]
e_gcd = [gcd(A[-1], A[-2])]

for i in range(2, N - 1):
    f_gcd.append(gcd(f_gcd[i - 2], A[i]))
    e_gcd.append(gcd(e_gcd[i - 2], A[-i - 1]))


print(f_gcd, e_gcd)

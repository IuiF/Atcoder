N = int(input())
S = list(map(int, input().split()))[::-1]
ans = []
for i in range(N - 1):
    ans.append(S[i] - S[i + 1])
ans.append(S[-1])
print(*ans[::-1])

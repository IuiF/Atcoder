N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]
S.sort(key=lambda x: x[1], reverse=True)

if S[0][0] != S[1][0]:
    ans = S[0][1] + S[1][1]
else:
    ans = S[0][1] + S[1][1] // 2


for i in range(2, N):
    if S[0][0] != S[i][0]:
        ans = max(ans, S[0][1] + S[i][1])
    else:
        ans = max(ans, S[0][1] + S[i][1] // 2)


print(ans)


# N = int(input())
# ans = 0

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# if a[0] != b[0]:
#     ans = a[1] + b[1]
# else:
#     ans = a[1] + b[1] // 2

# for _ in range(N - 2):
#     f, s = map(int, input().split())
#     tmp = ans
#     if a[1] == min(a[1], b[1]):
#         if b[0] != f:
#             ans = max(ans, b[1] + s)
#         else:
#             ans = max(ans, b[1] + s // 2)
#         if ans != tmp:
#             a[0], a[1] = f, s
#     else:
#         if a[0] != f:
#             ans = max(ans, a[1] + s)
#         else:
#             ans = max(ans, a[1] + s // 2)
#         if ans != tmp:
#             b[0], b[1] = f, s


# print(ans)

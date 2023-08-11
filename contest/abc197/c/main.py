N = int(input())
A = list(map(int, input().split()))
ans = 10**10


for i in range(2 ** (N - 1)):
    sub = []
    tmp = A[0]
    idx = 1

    for j in range(N - 1):
        if (i >> j) & 1:
            tmp |= A[idx]
        else:
            sub.append(tmp)
            tmp = A[idx]
        idx += 1

    sub.append(tmp)

    xor_result = sub[0]
    for s in sub[1:]:
        xor_result ^= s

    ans = min(ans, xor_result)

print(ans)

# 以下TLE

# N = int(input())
# A = list(input().split())
# ans = 10**10


# for i in range(2 ** (N - 1)):
#     sub = []
#     tmp = ["("]
#     idx = 0
#     for j in range(N - 1):
#         if (i >> j) & 1:
#             tmp.append(A[idx])
#             tmp.append("|")
#             idx += 1
#         else:
#             tmp.append(A[idx])
#             idx += 1
#             sub.append("".join(tmp))
#             sub.append(")^")
#             tmp = ["("]

#     if len(tmp) > 1:
#         tmp.append(A[idx])
#         sub.append("".join(tmp))
#         sub.append(")")
#     else:
#         sub.append(A[idx])

#     sub_str = "".join(sub)

#     ans = min(ans, eval(sub_str))

# print(ans)

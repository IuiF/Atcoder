A, B = map(int, input().split())
# A = bin(A)[2:].rjust(3, "0")
# B = bin(B)[2:].rjust(3, "0")
# ans = 0
# for i in range(3):
#     if int(A[i]) or int(B[i]):
#         ans += 2 ** (2 - i)

# print(ans)
print(A | B)

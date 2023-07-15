def NAND(x, y):
    return bool(not x or not y)


N = int(input())
S = list(input())
ans = S.count("1")

results = [S]

while N != 1:
    A = [int(NAND(int(S[0]), int(S[1])))]
    for i in range(2, N):
        A.append(int(NAND(int(A[-1]), int(S[i]))))
    S = A
    N = len(S)
    ans += S.count(1)
    results.append(S)

print(ans)

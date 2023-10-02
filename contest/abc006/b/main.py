N = int(input())
L = [0, 0, 1]
for i in range(N - 3):
    tmp = (L[-3] + L[-2] + L[-1]) % 10007
    L.append(tmp)

print(L[N - 1])

N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
ave_H = []
for i in range(N):
    ave_H.append(abs(T - H[i] * 0.006 - A))

print(ave_H.index(min(ave_H)) + 1)

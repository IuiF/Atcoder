N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
winner = -1
tmp = 0

for i in range(N):
    if C[i] == T and R[i] > tmp:
        winner = i
        tmp = R[i]

if winner == -1:
    for i in range(N):
        if C[i] == C[0] and R[i] > tmp:
            winner = i
            tmp = R[i]

print(winner + 1)

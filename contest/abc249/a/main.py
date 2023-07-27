A, B, C, D, E, F, X = map(int, input().split())
taka = 0
ao = 0
t = 0
while t < X:
    if t % (A + C) <= A:
        taka += B
    if t % (D + F) <= D:
        ao += E
    t += 1

print("Takahashi" if taka > ao else "Aoki" if ao > taka else "Draw")

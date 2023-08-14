N = input()
S = 0
for i in list(N):
    S += int(i)

print("Yes" if int(N) % S == 0 else "No")

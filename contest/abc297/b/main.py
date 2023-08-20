S = list(input())
B = []
R = []
K = []
for i in range(len(S)):
    if S[i] == "B":
        B.append(i + 1)
    if S[i] == "R":
        R.append(i + 1)
    if S[i] == "K":
        K.append(i + 1)
if B[0] % 2 != B[1] % 2 and R[0] < K[0] < R[1]:
    print("Yes")
else:
    print("No")

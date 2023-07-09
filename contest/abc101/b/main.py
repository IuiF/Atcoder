M = list(input())
N = 0
for i in M:
    N += int(i)
M = int("".join(M))
if M % N == 0:
    print("Yes")
else:
    print("No")

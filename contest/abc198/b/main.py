N = list(input())
for i in range(len(N)):
    if N[-1] == "0":
        N.pop()
    else:
        break

if N == N[::-1]:
    print("Yes")
else:
    print("No")

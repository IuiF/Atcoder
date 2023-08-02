N = int(input())
S = input()

if (len(S)) > N:
    print(S[:N], "...", sep="")
else:
    print(S)

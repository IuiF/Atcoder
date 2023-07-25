R, C = map(int, input().split())
A, AA = map(int, input().split())
B, BB = map(int, input().split())

if R == 1:
    if C == 1:
        print(A)
    else:
        print(AA)
else:
    if C == 1:
        print(B)
    else:
        print(BB)

N, P, Q = map(int, input().split())
D = list(map(int, input().split()))
if P > Q + min(D):
    print(Q + min(D))
else:
    print(P)

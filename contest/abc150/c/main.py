from math import factorial


def perm_order(perm):
    order = 0
    for i in range(len(perm)):
        smaller = sum(x < perm[i] for x in perm[i + 1 :])
        order += smaller * factorial(len(perm) - i - 1)
    return order + 1


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

print(abs(perm_order(P) - perm_order(Q)))

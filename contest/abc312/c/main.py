from collections import defaultdict


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)

A_dic = defaultdict(int)
B_dic = defaultdict(int)
for i in A:
    A_dic[i] += 1
for i in B:
    B_dic[i] += 1


AA = []
for k, v in A_dic.items():
    try:
        AA.append((k, v + AA[-1][1]))  # type: ignore
    except IndexError:
        AA.append((k, v))  # type: ignore

BB = []
for k, v in B_dic.items():
    try:
        BB.append((k, v + BB[-1][1]))  # type: ignore
    except IndexError:
        BB.append((k, v))  # type: ignore

for i in AA:
    for j in BB:
        if i[0] <= j[0] and i[1] >= j[1]:
            print(i[0])
            exit()
print(B[0] + 1)


# print(AA)
# print(BB)


# AA_d = dict(AA[1:])
# BB_d = dict(BB[1:])


# for ak, av in AA_d.items():
#     for bk, bv in BB_d.items():
#         if ak <= bk and av >= bv:
#             print(ak)
#             exit()

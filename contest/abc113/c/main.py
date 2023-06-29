N, M = map(int, input().split())
P_list = [[0] for _ in range(N + 1)]
P = [[0]]

for _ in range(M):
    tmp = list(map(int, input().split()))
    P_list[tmp[0]].append(tmp[1])
    P.append(tmp)

sorted_list = [sorted(P_list[i]) for i in range(N + 1)]

ids = [""] * M
for i in range(1, M + 1):
    p, y = P[i]
    y_pos = sorted_list[p].index(y)
    ids[i - 1] = "{:06d}{:06d}".format(p, y_pos)

for id in ids:
    print(id)

# print(
#     *[
#         "{:06d}{:06d}".format(P[i][0], sorted_list[P[i][0]].index(P[i][1]))
#         for i in range(1, M + 1)
#     ],
#     sep="\n"
# )

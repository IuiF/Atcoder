N, Q = map(int, input().split())
S = input()
Req_list = [list(map(int, input().split())) for _ in range(Q)]
AC_counts = [0] * (N + 1)


for i in range(1, N):
    if S[i - 1 : i + 1] == "AC":
        AC_counts[i] = AC_counts[i - 1] + 1
    else:
        AC_counts[i] = AC_counts[i - 1]

for i in range(Q):
    count = AC_counts[Req_list[i][1] - 1] - AC_counts[Req_list[i][0] - 1]
    print(count)

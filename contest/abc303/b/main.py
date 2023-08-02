from itertools import combinations

N, M = map(int, input().split())

peoples = list(range(1, N + 1))
Discord_list = list(combinations(peoples, 2))
check_list = []

for _ in range(M):
    tmp_list = list(map(int, input().split()))
    for i in range(N - 1):
        tmp = [tmp_list[i], tmp_list[i + 1]]
        tmp.sort()

        check_list.append(tuple(tmp))


check_list = list(set(check_list))

for i in check_list:
    Discord_list.remove(i)

print(len(Discord_list))

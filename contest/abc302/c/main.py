import itertools


def count_diff(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count


n, m = map(int, input().split())
ar = [input() for _ in range(n)]
arr = list(itertools.permutations(ar))

flag = False
for i in arr:
    f = True
    for j in range(1, len(i)):
        if count_diff(i[j - 1], i[j]) == 1:
            continue
        else:
            f = False
            break
    if f:
        flag = True
        break


print("Yes" if flag else "No")

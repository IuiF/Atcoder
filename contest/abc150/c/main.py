from itertools import permutations


n = int(input())
ar = [i + 1 for i in range(n)]
all_ar = list(permutations(ar))
all_ar.sort()

a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))


print(abs(all_ar.index(a) - all_ar.index(b)))

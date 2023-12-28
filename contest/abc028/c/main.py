import itertools


a = list(map(int, input().split()))
b = list(itertools.permutations(a, 3))
c = [sum(i) for i in b]
c = list(set(c))
c.sort()
print(c[-3])

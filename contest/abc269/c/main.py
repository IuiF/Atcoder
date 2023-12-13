import itertools

n = int(input())
n2 = bin(n)[2:][::-1]

ones = [i for i in range(len(n2)) if n2[i] == "1"]

combinations = []
for r in range(len(ones) + 1):
    combinations.extend(itertools.combinations(ones, r))

ans = []

for i in combinations:
    t = []
    for j in range(len(n2)):
        if j in i:
            t.append("1")
        else:
            t.append("0")
    t = t[::-1]
    t = int("".join(t), 2)
    ans.append(t)

ans.sort()
print(*ans, sep="\n")

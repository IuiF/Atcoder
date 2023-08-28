N = int(input())
A = set(list(map(int, input().split())))
B = list(A)
B.sort()

for i in range(len(B)):
    if i != B[i]:
        print(i)
        exit()
print(len(B))

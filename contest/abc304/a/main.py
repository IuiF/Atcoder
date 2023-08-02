num = int(input())
a,b = [],[]
for _ in range(num):
    tmp = list(input().split())
    a.append(tmp[0])
    b.append(int(tmp[1]))

X = b.index(min(b)) #bの最小値の位置を探す

print(*a[X:],*a[:X],sep='\n')

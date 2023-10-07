n = int(input())
a = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))
p.extend(a)
if len(set(p)) == k + 2:
    print("YES")
else:
    print("NO")

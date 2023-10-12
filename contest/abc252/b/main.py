n, k = map(int, input().split())
a = list(map(int, input().split()))
MAX = max(a)
A = set()
for i in range(n):
    if a[i] == MAX:
        A.add(i + 1)
b = list(map(int, input().split()))
for i in A:
    if i in b:
        print("Yes")
        exit()
print("No")

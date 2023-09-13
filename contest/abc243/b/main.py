n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans_0 = 0
for i in range(n):
    if a[i] == b[i]:
        ans_0 += 1

st_a = set(a)
st_b = set(b)
ans_1 = len(st_a.intersection(st_b)) - ans_0
print(ans_0)
print(ans_1)

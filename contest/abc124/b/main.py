n = int(input())
H = list(map(int, input().split()))
tmp_max = 0
count = 0
for i in range(n):
    if H[i] >= tmp_max:
        tmp_max = H[i]
        count += 1
print(count)

N = int(input())
lst = list(map(int, input().rstrip().split()))
ans = 0
i = 0
while i < N:
    tmp = 0
    j = i + 1
    while j < N and lst[i] >= lst[j]:
        tmp += 1
        i = j
        j += 1

    ans = max(ans, tmp)

    i = j

print(ans)

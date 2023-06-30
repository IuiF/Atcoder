S = list(input())
lst = []

i = 0
while i < len(S):
    j = i + 1
    while j < len(S) and S[i] == S[j]:
        j += 1
    lst.append((S[i], j - i))
    i = j

ans = []
i = 0
while i < len(lst):
    for j in range(lst[i][1] - 1):
        ans.append(0)

    tmp_max = max(lst[i][1], lst[i + 1][1])
    tmp_min = min(lst[i][1], lst[i + 1][1])
    if (tmp_max - tmp_min) % 2 == 0:
        ans.append(tmp_min + (tmp_max - tmp_min) // 2)
        ans.append(tmp_min + (tmp_max - tmp_min) // 2)
    elif lst[i][1] % 2 == 0:
        ans.append(tmp_min + (tmp_max - tmp_min) // 2)
        ans.append(tmp_min + (tmp_max - tmp_min) // 2 + 1)
    else:
        ans.append(tmp_min + (tmp_max - tmp_min) // 2 + 1)
        ans.append(tmp_min + (tmp_max - tmp_min) // 2)

    for j in range(lst[i + 1][1] - 1):
        ans.append(0)

    i += 2

# print(lst)
print(*ans)

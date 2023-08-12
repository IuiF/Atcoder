n = int(input())
arr = []
for _ in range(n):
    input()
    a = list(map(int, input().split()))
    arr.append(a)

x = int(input())
ans = []
for i in range(n):
    if x in arr[i]:
        ans.append((i + 1, len(arr[i])))

if len(ans) == 0:
    print(0)
    print()
    exit()

ans.sort(key=lambda x: x[1])
min_second_element = min(item[1] for item in ans)
ans = [item[0] for item in ans if item[1] == min_second_element]

print(len(ans))
print(*ans)

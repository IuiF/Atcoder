N = int(input())
ans = set()

for _ in range(N):
    tmp = input()
    if tmp in ans:
        ans.remove(tmp)
    else:
        ans.add(tmp)

print(len(ans))

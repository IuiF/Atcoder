N = int(input())
G = [[] for _ in range(N + 1)]
A = list(map(int, input().split()))

for i in range(N):
    G[i + 1].append(A[i])

arr = [1]
tmp = 1
for _ in range(N * 2):
    arr.append(G[tmp][0])
    tmp = arr[-1]

st = set()
for i in range(len(arr)):
    if arr[i] in st:
        tmp = arr[i]
        break
    else:
        st.add(arr[i])

ans = []
tmp = arr.index(tmp)
ans.append(arr[tmp])
while True:
    tmp += 1
    if arr[tmp] == ans[0]:
        break
    ans.append(arr[tmp])

print(len(ans))
print(*ans)

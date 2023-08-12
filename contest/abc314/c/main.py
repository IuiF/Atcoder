n, m = map(int, input().split())
s = list(input())
c = list(map(int, input().split()))

arr = [[] for _ in range(m)]
for i in range(n):
    arr[c[i] - 1].append(s[i])
for i in range(m):
    arr[i] = arr[i][::-1]

ans = []
st = set()
for i in range(n):
    if c[i] in st:
        ans.append(arr[c[i] - 1].pop())
    else:
        st.add(c[i])
        ans.append(arr[c[i] - 1][0])

print(*ans, sep="")

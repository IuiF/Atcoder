n = int(input())
s = input()
t = 0
arr = []
while t < n:
    q = t + 1
    while q < n and s[t] == s[q]:
        q += 1
    arr.append((s[t], q - t))
    t = q
arr.sort(key=lambda x: (x[0], -x[1]))

ans = 0
st = set()
for i in range(len(arr)):
    if arr[i][0] not in st:
        ans += arr[i][1]
        st.add(arr[i][0])
print(ans)

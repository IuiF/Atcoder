n = int(input())
a = list(map(int, input().split()))
b2 = []
b3 = []
st = set()
ans = 0

for i in a:
    x, y = 0, 0
    while i % 2 == 0:
        i //= 2
        x += 1
    while i % 3 == 0:
        i //= 3
        y += 1
    b2.append(x)
    b3.append(y)
    st.add(i)

if len(st) != 1:
    print(-1)
else:
    ans += sum(i - min(b2) for i in b2)
    ans += sum(i - min(b3) for i in b3)
    print(ans)

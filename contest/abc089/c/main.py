from itertools import combinations


n = int(input())
st = [set(), set(), set(), set(), set()]
for _ in range(n):
    s = input()
    if s[0] == "M":
        st[0].add(s)
    elif s[0] == "A":
        st[1].add(s)
    elif s[0] == "R":
        st[2].add(s)
    elif s[0] == "C":
        st[3].add(s)
    elif s[0] == "H":
        st[4].add(s)

for i in range(4, -1, -1):
    if st[i] == set():
        st.pop(i)


# if len(st) < 3:
#     print(0)
#     exit()

arr = list(combinations(st, 3))
ans = 0
for i in arr:
    t = 1
    for j in i:
        t *= len(j)
    ans += t


print(ans)

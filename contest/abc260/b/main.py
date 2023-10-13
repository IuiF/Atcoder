n, a, b, c = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
X = []
Y = []
for i in range(n):
    X.append((x[i], i))
    Y.append((y[i], i))
Z = list((x[i] + y[i], i) for i in range(n))
X.sort(key=lambda X: (X[0], -X[1]), reverse=True)
Y.sort(key=lambda Y: (Y[0], -Y[1]), reverse=True)
Z.sort(key=lambda Z: (Z[0], -Z[1]), reverse=True)
st = set()

for i in range(n):
    if a == 0:
        break
    if X[i][1] in st:
        continue
    else:
        st.add(X[i][1])
        a -= 1

for i in range(n):
    if b == 0:
        break
    if Y[i][1] in st:
        continue
    else:
        st.add(Y[i][1])
        b -= 1

for i in range(n):
    if c == 0:
        break
    if Z[i][1] in st:
        continue
    else:
        st.add(Z[i][1])
        c -= 1

st = list(st)
st.sort()
for i in st:
    print(i + 1)

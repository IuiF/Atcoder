N = int(input())
S = list(input())
p = [0, 0]
st = {tuple(p)}

for i in S:
    if i == "R":
        p[0] += 1
    elif i == "L":
        p[0] -= 1
    elif i == "U":
        p[1] += 1
    else:
        p[1] -= 1

    if tuple(p) in st:
        print("Yes")
        exit()
    st.add(tuple(p))

print("No")

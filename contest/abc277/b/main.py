n = int(input())
st = set()
for _ in range(n):
    s = input()
    if s in st:
        print("No")
        exit()
    elif s[0] in ["H", "D", "C", "S"] and s[1] in [
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "T",
        "J",
        "Q",
        "K",
    ]:
        st.add(s)
        continue
    else:
        print("No")
        exit()
print("Yes")

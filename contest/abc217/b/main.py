st = set()
for _ in range(3):
    st.add(input())
ST = set(["ABC", "ARC", "AGC", "AHC"])

print((ST - st).pop())

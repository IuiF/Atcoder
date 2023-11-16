n = int(input())
st = set()
for i in range(2, int(n**0.5) + 1):
    a = i
    while True:
        if a * i <= n:
            st.add(a * i)
        else:
            break
        a *= i


print(n - len(st))

n = int(input())
a = set()
b = set()
for _ in range(n):
    t = input()
    if t[0] == "!":
        a.add(t[1:])
    else:
        b.add(t)
if a & b:
    c = a & b
    print(c.pop())
else:
    print("satisfiable")

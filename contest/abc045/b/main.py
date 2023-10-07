a = input()
b = input()
c = input()
pa, pb, pc = 0, 0, 0
p = "a"

while True:
    if p == "a":
        try:
            p = a[pa]
        except IndexError:
            print("A")
            exit()
        pa += 1
    elif p == "b":
        try:
            p = b[pb]
        except IndexError:
            print("B")
            exit()
        pb += 1
    else:
        try:
            p = c[pc]
        except IndexError:
            print("C")
            exit()
        pc += 1

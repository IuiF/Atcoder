a, b, w = map(int, input().split())
w *= 1000
max_m = -1
min_m = -1

if w // a == w // b and (w % a != 0 or w % b != 0):
    print("UNSATISFIABLE")
    exit()


max_m = w // a


if w % b == 0:
    min_m = w // b
else:
    min_m = (w // b) + 1

print(min_m, max_m)

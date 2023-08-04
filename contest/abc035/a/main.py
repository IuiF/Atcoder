from math import gcd


w, h = map(int, input().split())
g = gcd(w, h)
w //= g
print("4:3" if w == 4 else "16:9")

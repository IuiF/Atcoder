num = int(input())
X = input()
Y = input()

X = X.replace("1", "l").replace("0", "o")
Y = Y.replace("1", "l").replace("0", "o")

print("Yes" if X == Y else "No")

n = bin(int(input()))

for i in range(len(n)):
    if n[-1 - i] == "1":
        print(i)
        exit()
print(1)

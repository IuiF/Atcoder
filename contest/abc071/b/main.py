S = list(input())
st = set(S)

for i in range(26):
    if chr(ord("a") + i) not in st:
        print(chr(ord("a") + i))
        exit()

print("None")

S = list(input())
for i in S:
    if i in "aeiou":
        continue
    else:
        print(i, end="")
print()

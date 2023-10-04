s = list(input())
a = []
for i in s:
    a.append(i.lower())
a[0] = a[0].upper()
print("".join(a))

s = list(input())
st = set(s)
if len(st) == len(s) and any(c.isupper() for c in st) and any(c.islower() for c in st):
    print("Yes")
else:
    print("No")

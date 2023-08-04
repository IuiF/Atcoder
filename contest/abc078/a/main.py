a = list(input().split())
if a[0] == a[1]:
    print("=")
elif sorted(a) == a:
    print("<")
else:
    print(">")

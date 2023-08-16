s = input()
if s.count(".") == 1:
    print(s[: s.index(".")])
else:
    print(s)

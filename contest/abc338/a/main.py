s = input()
if s[0].isupper() and s[1:].islower():
    print("Yes")
elif len(s) == 1 and s[0].isupper():
    print("Yes")
else:
    print("No")

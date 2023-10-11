s = input()
a = int(s[0] + s[1])
b = int(s[2] + s[3])
if 1 <= a <= 12 and 1 <= b <= 12:
    print("AMBIGUOUS")
elif 1 <= a <= 12:
    print("MMYY")
elif 1 <= b <= 12:
    print("YYMM")
else:
    print("NA")

s = input()
if s[0] == "A" and s.count("C") == 1 and "C" in s[2:-1]:
    for i in range(1, len(s)):
        if not s[i].islower() and i != s.index("C"):
            print("WA")
            break
    else:
        print("AC")
else:
    print("WA")

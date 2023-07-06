# 6 > 5 > 6 > ...
a = int(input())
if a % 11 == 0:
    print(int(a // 11) * 2)
elif a % 11 <= 6:
    print(int(a // 11) * 2 + 1)
else:
    print(int(a // 11) * 2 + 2)

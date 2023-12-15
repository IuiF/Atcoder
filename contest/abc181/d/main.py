from collections import Counter


s = input()
dic = Counter(s)

if len(s) == 1:
    print("Yes" if int(s) % 8 == 0 else "No")
    exit()
elif len(s) == 2:
    print("Yes" if (int(s) % 8 == 0 or int(s[::-1]) % 8 == 0) else "No")
    exit()


found = False
for i in range(1, 1000):
    if i % 8 == 0:
        i_str = str(i).zfill(3)
        if Counter(i_str) & dic == Counter(i_str):
            found = True
            break

if found:
    print("Yes")
else:
    print("No")

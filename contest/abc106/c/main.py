s = list(input())
k = int(input())
if len(set(s)) == 1:
    print(s[0])
else:
    for i in range(k):
        if s[i] == "1" and i == k - 1:
            print(1)
        elif s[i] != "1":
            print(s[i])
            exit()

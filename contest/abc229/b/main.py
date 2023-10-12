a, b = input().split()
a, b = str(min(int(a), int(b))), str(max(int(a), int(b)))
a, b = a[::-1], b[::-1]
for i in range(len(a)):
    if int(a[i]) + int(b[i]) >= 10:
        print("Hard")
        exit()
print("Easy")

s = "b"
n = int(input())
a = input()

for i in range(50):
    if a == s:
        print(i)
        exit()
    else:
        if i % 3 == 0:
            s = "a" + s + "c"
        elif i % 3 == 1:
            s = "c" + s + "a"
        else:
            s = "b" + s + "b"
print(-1)

n = int(input())
a = list(map(int, input().split()))
print(0)
for i in a:
    a = i * 2
    b = i * 2 + 1
    print(len(bin(a)[2:]) - 1)
    print(len(bin(b)[2:]) - 1)

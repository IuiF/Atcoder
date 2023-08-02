num = int(input())
num_tuple = tuple(map(int, input().split()))

Ans = 0

for i in num_tuple:
    tmp = 0
    while True:
        if i / 2 == int(i / 2):
            i /= 2
            tmp += 1
        else:
            break
    Ans += tmp

print(Ans)

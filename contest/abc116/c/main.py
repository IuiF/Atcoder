N = int(input())
lst = list(map(int, input().split()))
ans = 0
i = 0

while True:
    i = 0
    while True:
        if i == N:
            print(ans)
            exit()
        elif lst[i] == 0:
            i += 1
        else:
            break
    while i < N and lst[i] != 0:
        lst[i] -= 1
        i += 1
    ans += 1

print(ans)

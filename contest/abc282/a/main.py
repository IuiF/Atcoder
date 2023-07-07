A, B = map(int, input().split())
ans = ""
i = 1
while True:
    if B // 2**i == 0:
        break
    elif B % 2**i == 1:
        ans += "1"
    else:
        ans += "0"
    i += 1

print(ans[::-1])

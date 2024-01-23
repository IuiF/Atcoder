s = [list(input()) for _ in range(9)]
ans = 0

for i in range(2, 10):
    for j in range(10 - i):
        for k in range(10 - i):
            if (
                s[j][k]
                == s[j + i - 1][k]
                == s[j][k + i - 1]
                == s[j + i - 1][k + i - 1]
                == "#"
            ):
                ans += 1

print(ans)

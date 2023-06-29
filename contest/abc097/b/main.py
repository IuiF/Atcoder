X = int(input())
ans = 0
for i in range(1, 500):
    for j in range(2, 500):
        if i**j <= X:
            ans = max(ans, i**j)
        else:
            break

print(ans)

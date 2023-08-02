N = int(input())
check = "No"

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == N:
            check = "Yes"
            break
        else:
            continue

print(check)

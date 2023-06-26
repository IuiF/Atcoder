N = int(input())
for i in range(N):
    for j in range(N):
        if i * 4 + j * 7 == N:
            print("Yes")
            exit()
print("No")

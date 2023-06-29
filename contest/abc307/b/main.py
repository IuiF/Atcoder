N = int(input())
S_list = []
for _ in range(N):
    S_list.append(input())

for i in range(N):
    for j in range(i + 1, N):
        if (S_list[i] + S_list[j]) == (S_list[i] + S_list[j])[::-1] or (
            S_list[j] + S_list[i]
        ) == (S_list[j] + S_list[i])[::-1]:
            print("Yes")
            exit()
print("No")

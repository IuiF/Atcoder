N = int(input())
N_list = []

for _ in range(N):
    N_list.append(int(input()))

N_list = list(set(N_list))
N_list.sort(reverse=True)

print(len(N_list))

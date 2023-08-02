now = [0, 0]
N, M, H, K = map(int, input().split())
move_list = list(input())
cure_list = set()
for _ in range(M):
    cure_list.add(tuple(map(int, input().split())))

ans = "No"

for i in range(N):
    # move
    if move_list[i] == "U":
        now[1] += 1
    elif move_list[i] == "R":
        now[0] += 1
    elif move_list[i] == "D":
        now[1] -= 1
    else:
        now[0] -= 1

    # Health -1
    H -= 1

    if H < 0:
        break

    if tuple(now) in cure_list and H < K:
        cure_list.remove(tuple(now))
        H = K

    if i == N - 1:
        ans = "Yes"


print(ans)

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
a_t = [[a[j][i] for j in range(h)] for i in range(w)]
for j in range(w):
    print(*a_t[j], sep=" ")

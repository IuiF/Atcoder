n, q = map(int, input().split())
arr = [[i, 0] for i in range(n, 0, -1)]


for _ in range(q):
    n = list(input().split())
    if n[0] == "1":
        if n[1] == "R":
            arr.append([arr[-1][0] + 1, arr[-1][1]])
        elif n[1] == "L":
            arr.append([arr[-1][0] - 1, arr[-1][1]])
        elif n[1] == "U":
            arr.append([arr[-1][0], arr[-1][1] + 1])
        elif n[1] == "D":
            arr.append([arr[-1][0], arr[-1][1] - 1])
    else:
        print(*arr[-int(n[1])])

h, w, n = map(int, input().split())
M = [["." for _ in range(w)] for _ in range(h)]
now = [0, 0, "U"]

for _ in range(n):
    if M[now[0]][now[1]] == ".":
        M[now[0]][now[1]] = "#"

        if now[2] == "U":
            now[2] = "R"
            now[1] += 1
            if now[1] == w:
                now[1] = 0
        elif now[2] == "R":
            now[2] = "D"
            now[0] += 1
            if now[0] == h:
                now[0] = 0
        elif now[2] == "D":
            now[2] = "L"
            now[1] -= 1
            if now[1] == -1:
                now[1] = w - 1
        else:
            now[2] = "U"
            now[0] -= 1
            if now[0] == -1:
                now[0] = h - 1

    else:
        M[now[0]][now[1]] = "."
        if now[2] == "U":
            now[2] = "L"
            now[1] -= 1
            if now[1] == -1:
                now[1] = w - 1
        elif now[2] == "R":
            now[2] = "U"
            now[0] -= 1
            if now[0] == -1:
                now[0] = h - 1
        elif now[2] == "D":
            now[2] = "R"
            now[1] += 1
            if now[1] == w:
                now[1] = 0
        else:
            now[2] = "D"
            now[0] += 1
            if now[0] == h:
                now[0] = 0


for i in M:
    print("".join(i))

H, M = map(int, input().split())
q = ("s", "n", "u", "k", "e")
grid = []
pointer = [1, 1]

grid.append(["0" for _ in range(M + 2)])
for _ in range(H):
    grid.append(list("0" + input() + "0"))
grid.append(["0" for _ in range(M + 2)])

# while pointer != [H,M]:

#     if


print(grid)

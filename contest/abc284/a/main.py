N = int(input())
S = list(input() for _ in range(N))
print(*S[::-1], sep="\n")

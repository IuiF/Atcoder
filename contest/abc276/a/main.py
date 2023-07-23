S = list(input())
try:
    print(len(S) - S[::-1].index("a"))
except ValueError:
    print(-1)

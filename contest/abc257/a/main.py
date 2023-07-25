N, X = map(int, input().split())
print(chr(X // N + ord("A") - 1) if X % N == 0 else chr(X // N + ord("A")))

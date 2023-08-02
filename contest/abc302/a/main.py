A, B = map(int, input().split())
print(A // B + 1 if A % B != 0 else A // B)

A, B = map(int, input().split())
S = input()

try:
    tmp_a = int(S[:A])
    tmp_b = int(S[-B])
    if S[A] == "-":
        print("Yes")
    else:
        print("No")
except ValueError:
    print("No")

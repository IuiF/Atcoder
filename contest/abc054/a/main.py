D = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    1: 14,
}
A, B = map(int, input().split())
A = D[A]
B = D[B]
if A == B:
    print("Draw")
elif A > B:
    print("Alice")
else:
    print("Bob")

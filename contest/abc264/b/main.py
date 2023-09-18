r, c = map(int, input().split())
if r in [1, 15] or c in [1, 15]:
    print("black")
elif (r in [3, 13] and 3 <= c <= 13) or (c in [3, 13] and 3 <= r <= 13):
    print("black")
elif (r in [5, 11] and 5 <= c <= 11) or (c in [5, 11] and 5 <= r <= 11):
    print("black")
elif (r in [7, 9] and 7 <= c <= 9) or (c in [7, 9] and 7 <= r <= 9):
    print("black")
else:
    print("white")

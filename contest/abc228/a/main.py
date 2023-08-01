S, T, X = map(int, input().split())
if S > T:
    if S > X >= T:
        print("No")
    else:
        print("Yes")
elif S <= X < T:
    print("Yes")
else:
    print("No")

S = list(map(int, input().split()))
if sorted(S) == S and min(S) >= 100 and max(S) <= 675:
    if all(n % 25 == 0 for n in S):
        print("Yes")
        exit()
print("No")

N = int(input())
S = tuple(input())
win_count = N // 2 if N % 2 == 0 else N // 2 + 1
count = [0, 0]

for i in range(N):
    if S[i] == "T":
        count[0] += 1
    elif S[i] == "A":
        count[1] += 1

    if count[0] == win_count:
        print("T")
        break
    elif count[1] == win_count:
        print("A")
        break

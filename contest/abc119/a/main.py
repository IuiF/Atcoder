S = list(map(int, input().split("/")))
if S[0] < 2019:
    print("Heisei")
elif S[0] == 2019 and S[1] < 4:
    print("Heisei")
elif S[0] == 2019 and S[1] == 4 and S[2] <= 30:
    print("Heisei")
else:
    print("TBD")

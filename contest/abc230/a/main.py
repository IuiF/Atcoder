N = int(input())
if N > 41:
    N += 1
    print("AGC" + str(N).rjust(3, "0"))
else:
    print("AGC" + str(N).rjust(3, "0"))

num = int(input())
S = list(input())

for i in range(num):
    if S[i] == "|":
        i += 1
        while S[i] != "|":
            if S[i] == "*":
                print("in")
                exit()
            i += 1
        print("out")
        exit()

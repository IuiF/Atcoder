N = list(input())
op = ["+", "-"]

for i in range(2):
    for j in range(2):
        for k in range(2):
            if eval(N[0] + op[i] + N[1] + op[j] + N[2] + op[k] + N[3]) == 7:
                print(N[0] + op[i] + N[1] + op[j] + N[2] + op[k] + N[3] + "=7")
                exit()

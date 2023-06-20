N = int(input())
S = input()
ans_o = -1
ans_i = -1
i = 0
while i < N:
    j = i
    while j < N and S[j] == S[i]:
        j += 1

    if S[i] == "o" and j - i > ans_o:
        ans_o = j - i
    elif S[i] == "-" and j - i > ans_i:
        ans_i = j - i

    i = j

if ans_i == -1 or ans_o == -1:
    print(-1)
else:
    print(ans_o)

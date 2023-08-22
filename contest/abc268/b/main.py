S = list(input())
T = list(input())
ans = "Yes"
if len(S) > len(T):
    print("No")
    exit()
for i in range(len(S)):
    if S[i] != T[i]:
        ans = "No"
        break
print(ans)

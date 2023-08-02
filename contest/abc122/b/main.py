S = input().replace("A", "&").replace("T", "&").replace("C", "&").replace("G", "&")
Ans = 0

for i in range(len(S) + 1):
    if S.count(i * "&") > 0:
        Ans = i

print(Ans)

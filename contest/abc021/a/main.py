N = int(input())
ans = []
if N >= 8:
    N -= 8
    ans.append(8)
if N >= 4:
    N -= 4
    ans.append(4)
if N >= 2:
    N -= 2
    ans.append(2)
if N >= 1:
    N -= 1
    ans.append(1)
print(len(ans))
print(*ans, sep="\n")

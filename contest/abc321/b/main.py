import copy

n, x = map(int, input().split())
A = list(map(int, input().split()))
ans = -1

for i in range(0, 101):
    B = copy.copy(A)
    B.append(i)
    if (sum(B) - max(B) - min(B)) >= x:
        ans = i
        break

print(ans)

a = list(input())
a = [int(i) for i in a]
t = sum(a)
ans = 100 * t + 10 * t + t
print(ans)

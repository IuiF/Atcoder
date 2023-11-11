n, x = map(int, input().split())
s = list(map(int, input().split()))
print(sum(s[i] for i in range(n) if s[i] <= x))

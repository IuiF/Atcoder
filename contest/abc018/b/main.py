s = list(input())
n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    s[l - 1 : r] = s[l - 1 : r][::-1]
print("".join(s))

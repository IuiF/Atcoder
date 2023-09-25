n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = min(b) - max(a) + 1
print(ans if ans >= 0 else 0)

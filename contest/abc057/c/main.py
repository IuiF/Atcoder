n = int(input())
ans = 100

for i in range(1, int(n**0.5) + 2):
    a = n // i
    if n % i == 0:
        ans = min(ans, max(len(str(a)), len(str(i))))

print(ans)

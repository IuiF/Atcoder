n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

ans = sum(i for i in arr if i % 10 == 0)
tmp = sum(i for i in arr if i % 10 != 0)

try:
    if tmp % 10 == 0:
        tmp -= min(i for i in arr if i % 10 != 0)
except ValueError:
    print(0)
    exit()

print(ans + tmp)

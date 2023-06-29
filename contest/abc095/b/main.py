n, x = map(int, input().split())
Doughnuts = []
count = 0

for _ in range(n):
    Doughnuts.append(int(input()))

if x < sum(Doughnuts):
    print(0)
    exit()

x -= sum(Doughnuts)
count += n
count += x // min(Doughnuts)

print(count)

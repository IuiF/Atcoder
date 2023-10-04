n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i != 0:
        b.append(i)
print(int(sum(b) / len(b)) if (sum(b) % len(b)) == 0 else int(sum(b) / len(b)) + 1)

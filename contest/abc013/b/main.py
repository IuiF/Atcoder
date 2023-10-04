a = int(input())
b = int(input())
print(min(max(a, b) - min(a, b), min(a, b) + 10 - max(a, b)))

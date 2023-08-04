a = int(input())
b = int(input())
c = int(input())
arr = [a, b, c]
arr.sort(reverse=True)
print(arr.index(a) + 1)
print(arr.index(b) + 1)
print(arr.index(c) + 1)

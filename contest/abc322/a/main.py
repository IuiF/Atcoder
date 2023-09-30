n = int(input())
s = input()
try:
    print(s.index("ABC") + 1)
except ValueError:
    print(-1)

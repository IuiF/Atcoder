def solve(a, b, c):
    if c % 2 == 0 or (a > 0 and b > 0):
        return "<" if abs(a) < abs(b) else ">" if abs(a) > abs(b) else "="
    else:
        return "<" if a < b else ">" if a > b else "="


a, b, c = map(int, input().split())
print(solve(a, b, c))

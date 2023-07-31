def f(x):
    return x**2 + 2 * x + 3


n = int(input())
ans = f(f(f(n) + n) + f(f(n)))
print(ans)

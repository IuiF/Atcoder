def prime_value(value):
    n = int(value ** (1 / 2))
    if value < 2:
        return False
    for i in range(2, n + 1):
        if value % i == 0:
            return False
    return True


prime_list = [0 for _ in range(100001)]

for i in range(2, 100001):
    prime_list[i] = prime_list[i - 1]
    if prime_value(i) and prime_value((i + 1) // 2):
        prime_list[i] += 1

Q = int(input())

for i in range(Q):
    a, b = map(int, input().split())
    print(prime_list[b] - prime_list[a - 1])

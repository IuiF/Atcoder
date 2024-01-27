n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0

for a_meals in range(max(q[i] // a[i] if a[i] != 0 else 0 for i in range(n)) + 1):
    if any(q[i] < a_meals * a[i] for i in range(n)):
        continue

    rem_q = [q[i] - a_meals * a[i] for i in range(n)]

    b_meals = min((rem_q[i] // b[i]) if b[i] != 0 else float("inf") for i in range(n))

    ans = max(ans, a_meals + b_meals)

print(ans)

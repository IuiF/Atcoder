def generate(current, last_digit, length):
    if length == 0:
        num = int(current + "3")
        results.append(num)
        return

    for digit in range(last_digit, 4):
        generate(current + str(digit), digit, length - 1)


results = []
for length in range(0, 20):
    generate("", 1, length)

    if len(results) >= 333:
        break

n = int(input())

ans = sorted(results)[n - 1]

print(ans)

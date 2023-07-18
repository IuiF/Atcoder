N, K = map(int, input().split())
S = list(input())

zero_list = []
one_list = []

if S[0] == "0":
    one_list.append(0)

total = 0
ans = 0
p = 0

while True:
    count = 0
    if S[p] == "0":
        while p < len(S) and S[p] == "0":
            count += 1
            p += 1
        zero_list.append(count)
        total += count

        if len(zero_list) <= K:
            ans = max(ans, total)

    else:
        while p < len(S) and S[p] == "1":
            count += 1
            p += 1
        one_list.append(count)
        total += count

        if len(zero_list) > K:
            total -= zero_list.pop(0) + one_list.pop(0)

        if len(zero_list) <= K:
            ans = max(ans, total)

    if p == len(S):
        break

print(ans)

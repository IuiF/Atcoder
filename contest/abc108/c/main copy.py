N, K = map(int, input().split())
odd_num_arr = []
even_num_arr = []
ans = set()
t = K

if K % 2 == 0:
    K = K // 2

for i in range(1, 10**5):
    if i * K > N:
        break
    elif i % 2 == 0:
        even_num_arr.append(i * K)
    elif i % 2 == 1:
        odd_num_arr.append(i * K)


if t % 2 == 1:
    num_arr = sorted(odd_num_arr + even_num_arr)
    for i in num_arr:
        for j in num_arr:
            for k in num_arr:
                if abs(i - j) <= N or abs(i - k) <= N or abs(j - k) <= N:
                    ans.add((i, j, k))


else:
    for i in odd_num_arr:
        for j in odd_num_arr:
            for k in odd_num_arr:
                if abs(i - j) > N or abs(i - k) > N or abs(j - k) > N:
                    break
                ans.add((i, j, k))
    for i in even_num_arr:
        for j in even_num_arr:
            for k in even_num_arr:
                if abs(i - j) > N or abs(i - k) > N or abs(j - k) > N:
                    break
                ans.add((i, j, k))


print(len(ans))

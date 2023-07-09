T = int(input())


for _ in range(T):
    tmp = 0
    N, K = map(int, input().split())
    i = 40
    arr3 = [3**j for j in range(i + 1)]
    arr = [0] * (i + 1)

    while i >= 0:
        if N - arr3[i] >= 0:
            N -= arr3[i]
            arr[i] += 1
        else:
            arr3.pop()
            i -= 1

    if sum(arr) > K or (K - sum(arr)) % 2 == 1:
        print("No")
    else:
        print("Yes")
    # print(sum(arr))

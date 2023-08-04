N = int(input())
Ans = "Yes"
plans = [[0, 0, 0]]

for i in range(1, N + 1):
    plans.append(list(map(int, input().split())))

    if plans[i][0] % 2 != (plans[i][1] + plans[i][2]) % 2:
        Ans = "No"
        break
    elif (plans[i][0] - plans[i - 1][0]) < (
        abs(plans[i][1] - plans[i - 1][1]) + abs(plans[i][2] - plans[i - 1][2])
    ):
        Ans = "No"
        break

print(Ans)

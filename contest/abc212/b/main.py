x = list(input())
ans = None
if all(i == x[0] for i in x):
    ans = "Weak"
else:
    for i in range(1, 4):
        if (int(x[i - 1]) + 1 == int(x[i])) or (x[i - 1] == "9" and x[i] == "0"):
            ans = "Weak"
            continue
        else:
            ans = "Strong"
            break
print(ans)

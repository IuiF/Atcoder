a = input()
b = input()


if len(a) > len(b):
    ans = "GREATER"
elif len(a) < len(b):
    ans = "LESS"
else:
    for i in range(len(a)):
        if a[i] > b[i]:
            ans = "GREATER"
            break
        elif a[i] < b[i]:
            ans = "LESS"
            break

if a == b:
    ans = "EQUAL"

print(ans)

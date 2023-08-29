h, w = map(int, input().split())
for _ in range(h):
    tmp = list(map(int, input().split()))
    ans = []
    for i in tmp:
        if i == 0:
            ans.append(".")
        else:
            ans.append(chr(i + ord("A") - 1))
    print("".join(ans))

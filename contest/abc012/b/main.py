n = int(input())
ans = []
ans.append(str(n // 3600).rjust(2, "0"))
n %= 3600
ans.append(str(n // 60).rjust(2, "0"))
n %= 60
ans.append(str(n).rjust(2, "0"))
print(*ans, sep=":")

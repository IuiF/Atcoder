num = int(input())
s, t = input().split()
print(*[f"{s[i]}{t[i]}" for i in range(num)], sep="")

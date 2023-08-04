a = list(map(int, input().split()))
a.sort()
print(int(str(a[-1]) + str(a[-2])) + a[0])

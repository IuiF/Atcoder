S_num = list(map(int, input().split()))
print(*[chr(S_num[i] + 96) for i in range(len(S_num))], sep="")

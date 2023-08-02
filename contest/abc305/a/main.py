now_p = list(input())

if (0 <= int(now_p[-1]) <= 2) or (8 <= int(now_p[-1]) <= 9):
    now_p[-1] = '0'
else:
    now_p[-1] = '5'

print(*now_p,sep='')

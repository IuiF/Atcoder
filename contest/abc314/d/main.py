n = int(input())
s = list(input())
q = int(input())

dic = {}
flag = None
flag_num = 0

for i in range(q):
    a, b, c = input().split()
    a = int(a)
    if a == 1:
        b = int(b)
        dic[b - 1] = (c, i)
    elif a == 2:
        flag = False
        flag_num = i
    elif a == 3:
        flag = True
        flag_num = i

if flag is True:
    s = [v.upper() for v in s]
if flag is False:
    s = [v.lower() for v in s]


for k, v in dic.items():
    if v[1] <= flag_num:
        if flag is True:
            s[k] = v[0].upper()
        elif flag is False:
            s[k] = v[0].lower()
        elif flag is None:
            s[k] = v[0]
    else:
        s[k] = v[0]

print(*s, sep="")

s = input()
t = input()
dic = {}
dis = {}

for i in range(len(s)):
    if dic.get(t[i]) is None:
        dic[t[i]] = s[i]
    elif dic.get(t[i]) != s[i]:
        print("No")
        exit()

    if dis.get(s[i]) is None:
        dis[s[i]] = t[i]
    elif dis.get(s[i]) != t[i]:
        print("No")
        exit()

print("Yes")

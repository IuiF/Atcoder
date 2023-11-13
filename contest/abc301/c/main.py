from collections import defaultdict


s = input()
t = input()
sd = defaultdict(int)
td = defaultdict(int)
for i in range(len(s)):
    sd[s[i]] += 1
    td[t[i]] += 1
st = set(s + t)
st.discard("@")
flag = True
for i in st:
    a = sd[i]
    b = td[i]
    if a == b:
        continue
    elif a < b and i in "atcoder":
        if sd["@"] >= b - a:
            sd["@"] -= b - a
        else:
            flag = False
            break
    elif b < a and i in "atcoder":
        if td["@"] >= a - b:
            td["@"] -= a - b
        else:
            flag = False
            break
    else:
        flag = False
        break

print("Yes" if flag else "No")

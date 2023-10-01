w = input()
ans = []
for i in range(len(w)):
    if w[i] in ["a", "e", "i", "o", "u"]:
        continue
    else:
        ans.append(w[i])
print("".join(ans))

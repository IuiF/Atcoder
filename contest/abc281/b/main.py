S = list(input())
flag = True
if len(S) != 8:
    flag = False
elif not S[0].isalpha() or not ("".join(S[1:7])).isdigit() or not S[7].isalpha():
    flag = False
elif (
    not S[0].isupper()
    or not (100000 <= int("".join(S[1:7])) <= 999999)
    or not S[7].isupper()
):
    flag = False
print("Yes" if flag else "No")

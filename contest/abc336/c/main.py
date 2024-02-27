n = int(input()) - 1

n_base_5 = ""
while n > 0:
    n_base_5 = str(n % 5) + n_base_5
    n = n // 5
if n_base_5 == "":
    print(0)
    exit()


n = int(n_base_5) * 2

print(n)

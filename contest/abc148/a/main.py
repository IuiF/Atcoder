abc = "123"
for _ in range(2):
    tmp = input()
    if tmp == "1":
        abc = abc.replace("1", "")
    elif tmp == "2":
        abc = abc.replace("2", "")
    else:
        abc = abc.replace("3", "")

print(abc)

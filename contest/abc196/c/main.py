N = input()
len = len(N)
if len % 2 == 0:
    if int(N[: len // 2]) > int(N[len // 2 :]):
        print(int(N[: len // 2]) - 1)
    else:
        print(int(N[: len // 2]))
else:
    print("9" * (len // 2) if (len // 2) != 0 else "0")

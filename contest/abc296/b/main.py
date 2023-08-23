for i in range(9):
    a = input()
    if a.count("*"):
        b = a.index("*")
        print(chr(b + ord("a")) + str(9 - i - 1))
        exit()

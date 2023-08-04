keyword = input()
check = "NO"

while True:
    if keyword == "":
        check = "YES"
        break

    if keyword[-5:] == "dream" or keyword[-5:] == "erase":
        keyword = keyword[:-5]
    elif keyword[-7:] == "dreamer":
        keyword = keyword[:-7]
    elif keyword[-6:] == "eraser":
        keyword = keyword[:-6]
    else:
        break

print(check)

S = input()
on = ["Do", "Do", "Re", "Re", "Mi", "Fa", "Fa", "So", "So", "La", "La", "Si", "Do"]
ans: int = 0
li = "WBWBWWBWBWBW" * 100
for i in range(20):
    if li[i : i + 20] == S:
        print(on[i])
        exit()

N = input()

print(0 if (1000 - int(N[-3:]) == 1000) else 1000 - int(N[-3:]))

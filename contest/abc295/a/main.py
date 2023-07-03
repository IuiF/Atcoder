N = int(input())
W = list(input().split())
for S in W:
    if S in ["and", "not", "that", "the", "you"]:
        print("Yes")
        exit()

print("No")

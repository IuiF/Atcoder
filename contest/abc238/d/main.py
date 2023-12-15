n = int(input())
for _ in range(n):
    a, s = map(int, input().split())
    if 2 * a > s:
        print("No")
    else:
        bin_a = bin(a)[2:].zfill(60)
        bin_t = bin(s - 2 * a)[2:].zfill(60)
        if all(bin_a[i] == "0" for i in range(len(bin_t)) if bin_t[i] == "1"):
            print("Yes")
        else:
            print("No")

num = int(input())
num_list = list(map(int, input().split()))
Ans = 0

while all(i % 2 == 0 for i in num_list):
    num_list = [i / 2 for i in num_list]
    Ans += 1

print(Ans)

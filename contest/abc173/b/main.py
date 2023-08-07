from collections import defaultdict


N = int(input())
dic = defaultdict(int)
for _ in range(N):
    dic[input()] += 1
print("AC x " + str(dic["AC"]))
print("WA x " + str(dic["WA"]))
print("TLE x " + str(dic["TLE"]))
print("RE x " + str(dic["RE"]))

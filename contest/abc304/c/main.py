import math

N, D = map(int, input().split()) # N:人数 D:感染範囲

person = [] # x, y, 感染の有無
person.append([*map(int, input().split()), 'Yes'])

for _ in range(1,N):
    person.append([*map(int, input().split()), 'No']) # 残りの座標を追加

while True:
    tmp = False
    for i in range(0,N):
        for j in range(0,N):
            if i == j:
                continue
            tmp_check = format(math.sqrt(
                                        (person[i][0]-person[j][0])**2 +
                                        (person[i][1]-person[j][1])**2
                                        ), '.2f') # formatはstrになる
            if float(tmp_check) <= D and ( person[i][2] == 'Yes' or person[j][2] == 'Yes' ):
                if person[i][2] == 'No':
                    person[i][2] = 'Yes'
                    tmp = True
                if person[j][2] == 'No':
                    person[j][2] = 'Yes'
                    tmp = True
    if tmp != True:
        break

for k in range(N):
    print(person[k][2])

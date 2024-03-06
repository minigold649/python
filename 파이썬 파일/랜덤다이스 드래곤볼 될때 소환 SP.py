import random
r = random

dice = ['태풍', '달', '기어', '스위치', '태양']
count = 1000

sp = []
tsp = 0

for k in range(0, count):
    dicefd = [[0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], [0, 'x'], ]
    susp = 10
    db = False
    while(True):
        if (db == False):
            #주사위 소환
            for i in range(0, 15):
                n = r.randint(0, 4)
                if (dicefd[i] == [0, 'x']):
                    dicefd[i][1] = dice[n]
                    dicefd[i][0] += 1
                    susp += 10
            #print(dicefd)
            db = True
            #주사위 합치기
            for i in range(0, 14):
                for j in range(i, 14):
                    if (dicefd[i][0] != 7 and dicefd[i][1] != 'x' and dicefd[i][0] == dicefd[j+1][0] and dicefd[i][1] == dicefd[j+1][1]):
                        dicefd[i][0] += 1
                        dicefd[j+1] = [0, 'x']
                        db = False
                        continue
        else:
            break
    sp.append(susp)

'''dicefd.sort()
print(dicefd)'''
#print(sp)
for i in range(0, count):
    tsp += sp[i]

print("평균 소환 SP : ", int(tsp/count), sep="")
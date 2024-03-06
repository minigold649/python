import random
r = random

quelen = int(input("문제 수 : "))
que = []
ans = []
limit = int(quelen/5)+1
num = 0
print("\n")

i = 0
while(i < quelen):
    #print(que)
    num = 0
    n = r.randint(1, 5)
    if (i > 0):
        for j in range(0, i):
            #print(j)
            if (que[j] == n):
                num += 1
        if (num < limit):
            que.insert(0, n)
            i += 1
    else:
        que.insert(0, n)
        i += 1

for i in range(0, quelen):    
    print("\n", i+1, "번 문제\n➀ ➁ ➂ ➃ ➄", sep = "")
    a = int(input("-> "))
    ans.insert(0, a)

print(que)
print(ans)

score = 0
for i in range(0, quelen):
    if (que[i] == ans[i]):
        score += 100/quelen
print(score, "점" ,sep = "")
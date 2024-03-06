import random
r = random

num = 1000000
count = 100000

se = []
fail = 0
success = 0

def firstway(num, count, f, s):
    for j in range(0, count):
        se.clear()
        for i in range(0, num):
            se.append(0)

        n = r.randint(0, num-1)
        se[n] = 1
        
        a = r.randint(0, num-1)
        t = se[a]

        if (t == 1):
            f += 1
            print("실패!", j+1)
        else:
            s += 1
            print("성공!", j+1)
    return f, s

def secondway(num, count, f, s):
    for i in range(0, count):
        n = r.randint(0, num-1)
        if (n == 0):
            f += 1
            print("실패!", i+1)
        else:
            s += 1
            print("성공!", i+1)
    return f, s

#fail, success = firstway(num, count, 0, 0)
fail, success = secondway(num, count, 0, 0)

print("성공 : ", success/count*100, "%", sep = "")
print("실패 : ", fail/count*100, "%", sep = "")
print("총 횟수 : ", count, sep = "")
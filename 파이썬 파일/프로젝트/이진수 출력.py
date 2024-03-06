def ejinsu(n):
    while True:
        if (n == 0):
            elist.insert(0, 0)
            break
        elif (n == 1 or n == -1):
            elist.insert(0, 1)
            break
        elif (n % 2 == 0):
            elist.insert(0, 0)
            n /= 2
        elif (n % 2 == 1):
            elist.insert(0, 1)
            n -= 1
            n /= 2

elist = []
num = int(input("숫자 입력 : "))
ejinsu(num)
#print(elist)

le = len(elist)
if (elist[0] != 0):
    a = 1
    for i in range(1, le):
        a *= 10
    b = int(a/10)
    for i in range(1, le):
        if (elist[i] == 1):
            a += b
        b = int(b/10)
    if (num < 0):
        a *= -1
else:
    a = 0
print(num, "이진수 :", int(a))

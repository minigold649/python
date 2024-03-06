'''
플레이어 파일 형식
1. 확률
2. 강화
'''
import random as r
import os
from pathlib import Path

np = 20
new = True

def newpage (): # 새로운 페이지
    print("\n" * np)

def in_put(): # 입력받는 시스템
    tg = True
    n = input("-> ")
    a = list(n)
    if (len(a) != 0) :
        for i in range(len(a)):
            if (a[i] == '1' or a[i] == '2' or a[i] == '3' or a[i] == '4' or a[i] == '5' or a[i] == '6' or a[i] == '7' or a[i] == '8' or a[i] == '9' or a[i] == '0'):
                continue
            else:
                tg = False
                break
        if (tg):
            return int(n)
        else:
            return -1
    else:
        return -1

def nameinput():
    global name
    tri = True
    while (tri):
        name = input("닉네임을 입력하세요.\n-> ")
        na = list(name)
        if (len(na) != 0):
            tri = False
            for i in range(len(na)):
                if (na[i] == '/' or na[i] == '\\' or na[i] == '*' or na[i] == ':' or na[i] == '?' or na[i] == '"' or na[i] == '<' or na[i] == '>' or na[i] == '|'):
                    newpage()
                    print("사용 불가능한 닉네임입니다.\n\n")
                    tri = True
                    break
        else:
            newpage()
            print("잘못 입력하셨습니다.\n\n")
            continue
    newpage()
        

nameinput()

tri2 = True
for i in Path("D:\\").iterdir(): # 파일 검사
    i2 = str(i)
    fil = i2.replace("D:\\", "")
    if (fil == "강화게임파일"):
        tri2 = False
        break

if (tri2):
    os.mkdir("D:\강화게임파일") # 파일 생성

f = open("D:\강화게임파일\\NameList.txt", 'a') # 닉넴 리스트 파일 생성
f.close()

with open("D:\강화게임파일\\NameList.txt", 'r') as f: # 기존 유저인지 확인
    nl = f.read()
    nl = nl.split("\n")
    for i in range(0, len(nl)):
        if (name == nl[i]):
            new = False

if (new): # 새로운 유저
    with open("D:\강화게임파일\\NameList.txt", 'a') as f:
        f.write(f"{name}\n")
    with open(f"D:\강화게임파일\{name}.txt", 'w') as f:
        f.write("100\n0")
    print("안녕하세요..!")
    print("강화 게임에 오신것을 환영합니다!!\n")

# 값 불러오기
with open(f"D:\강화게임파일\{name}.txt", 'r') as f:
    p = f.read()
    p = p.split("\n")
    lvl = int(p[1])
    per = float(p[0])

# 실행
while (True):
    #print("강화 게임!\n")
    print(f"{name}  /  {lvl}강  /  성공확률 : {per}%")
    print('\n1 : 강화 / 2 : 게임종료')
    n = in_put()

    if (n == 1): # 강화
        perc = per*100
        ran = r.randint(1, 10000)
        
        if (perc >= ran): # 성공
            lvl += 1
            per = int(per * 90)/100
            newpage()
            print("강화성공!!\n")
        
        else: # 실패
            lvl -= 1
            per = 100
            for i in range(0, lvl):
                per = int(per*90)/100
            newpage()
            print("강화실패...\n")
    
    elif (n == 2):
        with open(f"D:\강화게임파일\{name}.txt", 'w') as f:
            f.write(f"{per}\n{lvl}")
        newpage()
        print("감사합니다")
        break

    else:
        newpage()
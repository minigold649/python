import os
from pathlib import Path

tri = True
for i in Path("D:\\").iterdir():
    i2 = str(i)
    file = i2.replace("D:\\", "")
    if (file == "Python txt file"):
        tri = False
        break

if (tri): 
    os.mkdir("D:\Python txt file")




name = "테스트파일"

with open(f"D:\Python txt file\{name}.txt", 'a') as f: # with를 벗어나는 순간 파일 자동닫힘
    for i in range(1, 11):
        f.write(f"{i}\n") # 쓰기


with open(f"D:\Python txt file\{name}.txt", 'a') as f:
    f.write(f"멍청이")

f = open(f"D:\Python txt file\{name}.txt", 'r')
# 파일 생성(있으면 그 파일사용)후 r(읽기) w(초기화 후 쓰기) a(마지막 이어서 쓰기)

a = f.readline() # 순서대로 파일 한줄 읽은 후 문자열로 저장
print(a)

#b = f.readlines() # 아직 안읽은 모든 줄을 읽은 후 리스트로 저장(문자열)
#print(b)

c = f.read() # 아직 안읽은 모든 줄을 읽은 후 저장(문자열)
c = c.split("\n") # 활용 가능성 있음
print(c)

f.close()
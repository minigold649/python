import os
from pathlib import Path

main = "이써현 주제에" # 파일 이름
wr = "이써현 주제에" # 텍스트 파일 내용
pos = "D:\\" # 파일생성경로

def sfil(pa, name):
    tri = True
    for i in Path(pa).iterdir():
        i2 = str(i)
        file = i2.replace(pa, "")
        if (file == name):
            tri = False
            return tri
    return tri


if (sfil(f"{pos}", main)):
    os.mkdir(f"{pos}{main}")

for i in range(1, 100+1):
    if (sfil(f"{pos}{main}\\", str(i))):
        os.mkdir(f"{pos}{main}\{i}")
    for j in range(1, 10+1):
        f = open(f"{pos}{main}\{i}\{j}.txt", 'w')
        for h in range(1, 100+1):
            f.write(f"{wr}\n")
        f.close

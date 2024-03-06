import os
from pathlib import Path

tri = True
for i in Path("D:\\").iterdir(): # 파일 있는지 검사
    i2 = str(i)
    file = i2.replace("D:\\", "")
    if (file == "테스트파일(삭제해도됨)"):
        tri = False
        break

if (tri): # 없으면 생성
    os.mkdir("D:\테스트파일(삭제해도됨)")
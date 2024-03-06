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


f = open("D:\Python txt file\에베베.txt", 'w')
n = 0
for i in range(1, 1000):
    n = i
    f.write(f"------------------------------------------ {i}\n")
    while(n!= 1 and n!= 2 and n!= 4):
        if (n % 2 == 0):
            n /= 2
        else:
            n = n * 3 + 1
        f.write(f"{str(int(n))} / ")
    f.write("\n")
f.close()
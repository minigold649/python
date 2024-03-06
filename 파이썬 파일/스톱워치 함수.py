import time
t = time
nt = 0
st = t.time()
while True:
    temp = t.time()
    tet = int(temp - st)
    if (nt < tet):
        nt = tet
        print(nt)
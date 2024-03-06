'''
사전 함수

test[??키] = ?? # ??키의 변수를 ??로 정한다.
test[??키] = test.get(??키)
del test[??키] # ??키를 삭제한다
test.get(??키, ??) # ??키의 변수가 있을경우 그대로 출력, 없을경우 ??를 출력 (정하는건 아님)
test.keys() # test의 있는 ??키를 모두 출력 
test.values() # test의 있는 ??키의 변수를 모두 출력
test.items() # test의 있는 ??키와 그 변수를 전부다 출력
??키 in test # test의 ??키가 있으면 True 없으면 False 출력
test.clear # 초기화

숫자 or 문자 = ??
'''
a = {512:"누군가", 649:"잇츠마이"}

print(a[512])
print(a.get(649))

a[42] = "이에에에"
del a[512]
print(a)

print(a.get(42, "ad"))
print(a.keys())
print(a.values())
print(a.items())
print(42 in a)
print(32 in a)

a["qwfd-34"] = "sdb"
a[649] = "허"
print(a)

a.clear()
print(a)
test = {'first':'hey', 'second':'why??', 'third':'no!!'}

print(test.keys()) # keys값을 dict_keys(리스트) 꼴로 출력
print(list(test.keys())) # keys값을 리스트 꼴로 출력
print(test.values()) # values값을 dict_values(리스트) 꼴로 출력
print(list(test.values())) # values값을 리스트 꼴로 출력

tli = list(test.values()) # 리스트로 완벽하게 변환됨
print(tli)
print(tli[0])

print(list(test.keys())[0]) #변환 안해줘도 이렇게 한다면 리스트처럼 사용가능

print(test.items()) # keys와 values를 한묶음씩 튜플로 묶은후 dict_times(리스트) 로 저장
tli2 = list(test.items()) # keys와 values를 한묶음씩 튜플로 묶은후 리스트 로 저장
print(tli2)
print(tli2[1][0])
tli2[2] = 'test' # 튜플 자체를 다른걸로 바꿀수 있음
print(tli2)
#tli2[0][1] = 'test22' # 튜플내부를 변경하려 해서 오류

print('second' in test) # keys중에 'second'가 있으면 True 아니면 False
print('hey' in test)

vt = test.get('first')
vt2 = test['second']
# test.get('XX') == test['XX'] # 둘다 'XX'라는 keys가 가진 values값을 가리킴
print(vt)
print(vt2)

test2 = {}
a = test.keys()
b = bool(a) # 불 형태로 전환해서 저장 (불로 전환할때 뭔가 비어있는 느낌이면 False 아니면 True)
print(b)
a = test2.keys()
b = bool(a)
print(b)

a, b = b, a # 서로 값을 바꿈
print(b)
print(a)

c, *d = (36, 354, 324, 3) # * <- 이 표시가 붙어있으면 나머지 뒤쪽을 합쳐서 리스트로 만들어 저장
print(c, d)
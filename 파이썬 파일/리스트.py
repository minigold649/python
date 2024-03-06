a = "에베벱베붸"
print(a[2:5]) # 2번째 부터 4번째 까지 출력

'''
리스트 함수들

index("test") # test가 어느 위치에 있는지 확인
insert(n, "test") # test를 n번째에 추가
append("test") # test를 제일 뒤쪽에 추가
pop(n) # n번째 변수 제거
count("test") # test가 몇개 있는지 확인
sort() # 순서대로 배열 (예 : 1,2,3,4,5.....)
reverse() # sort 반대 = sort(reverse = True)
clear() # 리스트 초기화
extend("text") # text를 한글자씩 분리해 뒤쪽에 추가 (예 : 't', 'e', 'x', 't')

주의 : n은 0번째 부터 시작
'''

tl = ["testdfd", "ab", "wow", "ye", "wa", "wa", "wa", "  ", "!@#", "/34", "&^#$에에"]

tl.insert(3, "흠")
print(tl)

tl.append("가사")
tl.append("ㅠㄴㄹ")
tl.append("가나다라")
tl.append("에베베")

print(tl)
tl.sort()
print(tl)
tl.pop(4)
print(tl)
print(tl.count("wa"))
tl.reverse()
print(tl)
tl.extend("dfdfe24ㄹ에라도f")
print(tl)
tl.sort()
print(tl)
tl.clear()
print(tl)

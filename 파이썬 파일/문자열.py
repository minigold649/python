a = "가나다다 다라라"

print(f"에베베{a}마바사") # f"문자{변수}문자"

print(a.count("다")) # 특정문자 개수
print(a.find("라")) # 특정문자가 처음나온 위치 (없으면 -1)
print(a.join("ㅁㅁㅁㅁ")) # 특정문자 사이사이에 {a} 집어넣음

a.upper() # 소문자 -> 대문자
a.lower() # 대문자 -> 소문자

a.lstrip() # 젤 왼쪽 공백 삭제
a.rstrip() # 젤 오른쪽 공백 삭제
a.strip() # 양쪽 공백 삭제

print(a.replace("다", "ek")) # 특정문자를 지정문자로 바꿈
print(a.split("다")) # 특정문자를 기준으로 분리 후 리스트로 변환
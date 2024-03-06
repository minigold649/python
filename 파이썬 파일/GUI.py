from tkinter import *
from os import *
from pathlib import Path

tri = True
for i in Path("D:\\").iterdir():
    i2 = str(i)
    file = i2.replace("D:\\", "")
    if (file == "gui 테스트"):
        tri = False
        break

if (tri):
    mkdir("D:\gui 테스트")


def bt3f():
    
    bt2.destroy() # 삭제기능

    # 레이블
    la1.config(text="ㅂㅇ", fg="red", bg="white") # 값 변경
    la2.config(image=ph2)

    # 텍스트 입력
    tg = txt.get("1.0", END)  # 텍스트값 얻기("1.0" -> 1번째줄 0번째)
    tg = tg.replace("\n", "") # 입력안한거 없애기
    eg = e.get() # 텍스트(1줄)값 얻기
    print(tg, eg, sep="\n")
    txt.delete("1.0", END) # 빈칸으로 만듬
    e.delete(0, END)

    # 리스트 박스
    lb.delete(1) # 특정자리 삭제
    print(lb.size()) # len() 이거랑 똑같음
    print(lb.get(0,2)) # 튜플로 범위내 값 얻음
    print(lb.curselection()) # 선택항목 위치값 얻음


win = Tk() # 창 생성

# 창 설정 --------------------------------------------------------------

win.title("gui 테스트!") # 창 제목
win.geometry("800x600+0+0") # 창크기 : 가로x세로 + x+y(위치)
win.resizable(False, False) # 가로 세로 길이 변경 True:가능 / False:불가능


# 버튼 ------------------------------------------------------------------------

bt1 = Button(win, padx=0, pady=0, width=5, height=2, text="버튼1", fg="#abffab", bg="black")
# 가로여백 / 세로여백 / 가로길이 / 세로길이 / 버튼문구 / 문자색 / 바탕색
bt1.pack() # 표시
bt1.place(x=400, y=300) # 버튼 위치

ph = PhotoImage(file="D:\gui 테스트\이미지 1.png")
ph2 = PhotoImage(file="D:\gui 테스트\이미지 2.png")

bt2 = Button(win, image=ph) # 그림적용 (width,height가 픽셀수로 작동)
bt2.pack()

bt3 = Button(win, width=5, height=2, command=bt3f) # 버튼클릭될때 함수 실행
bt3.pack()


# 레이블 -----------------------------------------------------------------------------------------

la1 = Label(win, text="하이", fg="#abffab", bg="blue") # 글자
la1.pack()

la2 = Label(win, image=ph) # 그림
la2.pack()


# 텍스트 입력 -----------------------------------------------------------------

txt = Text(win, width=20, height=4)
txt.pack()
txt.insert(END, "텍스트 파일처럼 입력가능")

e = Entry(win, width=20)
e.pack()
e.insert(0, "한줄만 입력가능")


# 리스트 박스 ------------------------------------------------------------------------

lb = Listbox(win, selectmode="extended", height=0) 
# single도 있음 /// 모드 / 몇개 보여질지(0은 모두)
lb.pack()
lb.insert(0, "a")
lb.insert(1, "b")
lb.insert(END, "c")
lb.insert(0, "d")


# 체크 버튼 ----------------------------------------------------------------------



win.mainloop()
import time as t
import random as r

up_plus_coin = 1 # 업그레이드 시 초당 돈 증가
up_cri_coin = 1 # 업그레이드 시 크리티컬 돈 증가 (%)
up_percri_coin = 0.5 # 업그레이드 시 크리티컬 확률 증가 (%) [고정값]

need_plus_coin = 1 # 초당 돈 업그레이드 비용
need_cri_coin = 100 # 크리티컬 돈 업그레이드 비용
need_percri_coin = 1000 # 크리티컬 확률 업그레이드 비용

coin = 100000000000 # 돈
plus_coin = 1 # 초당 돈
cri_coin = 10 # 크리티컬 돈 (%)
percri_coin = 1 # 크리티컬 확률 (%)

np = 20 # 새로운 페이지 간격
def newpage ():
    print("\n" * np)

# 업그레이드 함수
def upgrade (need_coin, n1, n2, n3, n4, suc, suc2):
    global coin, plus_coin, cri_coin, percri_coin, need_plus_coin, need_cri_coin, need_percri_coin, up_plus_coin, up_cri_coin, up_percri_coin
    if (coin >= need_coin):
        coin -= need_coin
        if (suc == 1 and suc2 == 0): # 초당 돈
            plus_coin += up_plus_coin
            up_plus_coin = up_plus_coin*n1 - int(up_plus_coin/n2)
            need_plus_coin = need_plus_coin*n3 - int(need_plus_coin/n4)
        elif (suc == 2 and suc2 == 1): # 크리티컬 확률
            percri_coin += up_percri_coin
            need_percri_coin = need_percri_coin*n3 - int(need_percri_coin/n4)
        elif (suc == 2 and suc2 == 2): # 크리티컬 돈
            cri_coin += up_cri_coin
            up_cri_coin += 1
            need_cri_coin = need_cri_coin*n3 - int(need_cri_coin/n4)
        print("업그레이드 성공!\n")
    else:
        print("돈 부족!\n")

def in_put ():
    tg = True
    n = input("-> ")
    a = list(n)
    for i in range(len(a)):
        if (a[i] == '1' or a[i] == '2' or a[i] == '3' or a[i] == '4' or a[i] == '5' or a[i] == '6' or a[i] == '7' or a[i] == '8' or a[i] == '9' or a[i] == '0'):
            continue
        else:
            tg = False
            break
    if (tg):
        return int(n)
    else:
        return 0

# 게임시작
print('돈 노가다 게임!\n\n')
while True:
    # 처음 메뉴
    print('..메인메뉴..')
    print(f"{coin}원 / 초당 : {plus_coin}원 / 크리티컬 확률 : {percri_coin}% / 크리티컬 돈 : {cri_coin}%")
    print('\n1 : 돈 모으기 / 2 : 업그레이드 / 3 : 게임종료\n')
    n = in_put()
    newpage()
    
    # 돈 모으기 (1)
    if (n == 1):
        print('돈 모으는 시간 (단위:초)\n')
        cointime = in_put()
        newpage()
        if (cointime != 0):
            start_time = t.time()
            i = 0
            while(i < cointime):
                now_time = t.time()
                sec = int(now_time - start_time)
                if (i < sec):
                    i += 1
                    wowcoin = r.randint(1, 1000)
                    if (wowcoin <= int(percri_coin*10)):
                        coin += plus_coin + int(plus_coin*(cri_coin/100))
                        print(f"{i}초 / +[{plus_coin + int(plus_coin*(cri_coin/100))}]원")
                    else:
                        coin += plus_coin
                        print(f"{i}초 / +{plus_coin}원")
            newpage()
        
        # 잘못 입력 (1 -> ?)
        else:
            print('잘못 입력 하셨습니다.\n')
    
    # 업그레이드 (2)
    elif (n == 2):
        esc2 = True
        while esc2:
            print('..업그레이드..')
            print('\n1 : 초당 버는 돈 / 2 : 크리티컬 / 3 : 취소\n')
            n2 = in_put()
            newpage()

            # 초당 돈 (2 -> 1)
            if (n2 == 1):
                esc2_1 = True
                while esc2_1:
                    print(f"{coin}원 / 초당 : {plus_coin}원")
                    print(f"[ 비용 : {need_plus_coin}원 / 초당 : +{up_plus_coin}원 ]")
                    print('\n1 : 업그레이드 / 2 : 취소\n')
                    n2_1 = in_put()
                    newpage()
                    
                    # 초당 돈 업글 (2 -> 1 -> 1)
                    if (n2_1 == 1):
                        upgrade(need_plus_coin, 2, 4, 3, 1.25, n2, 0) # 초당 돈 밸런스 (+초당 돈, 비용)
                    
                    # 초당 돈 나가기 (2 -> 1 -> 2)
                    elif (n2_1 == 2):
                        esc2_1 = False
                    
                    # 잘못 입력 (2 -> 1 -> ?)
                    else:
                        print('잘못 입력 하셨습니다.\n')

            # 크리티컬 (2 -> 2)
            elif (n2 == 2):
                esc2_2 = True
                while esc2_2:
                    print('..크리티컬..')
                    print('\n1 : 크리티컬 확률 / 2 : 크리티컬 돈 / 3 : 취소\n')
                    n2_2 = in_put()
                    newpage()

                    # 크리티컬 확률 (2 -> 2 -> 1)
                    if (n2_2 == 1):
                            esc2_2_1 = True
                            while esc2_2_1:
                                if (percri_coin < 80):
                                    print(f"{coin}원 / 크리티컬 확률 : {percri_coin}%")
                                    print(f"[ 비용 : {need_percri_coin}원 / 크리티컬 확률 : +{up_percri_coin}% ]")
                                    print('\n1 : 업그레이드 / 2 : 취소\n')
                                    n2_2_1 = in_put()
                                    newpage()
                            
                                    # 크리티컬 확률 업글 (2 -> 2 -> 1 -> 1)
                                    if (n2_2_1 == 1):
                                        upgrade(need_percri_coin, 0, 0, 2, 1.75, n2, n2_2) # 크리티컬 확률 밸런스 (X, 비용)

                                    # 크리티컬 확률 나가기 (2 -> 2 -> 1 -> 2)
                                    elif (n2_2_1 == 2):
                                        esc2_2_1 = False
                                    
                                    # 잘못 입력 (2 -> 2 -> 1 -> ?)
                                    else:
                                        print('잘못 입력 하셨습니다.\n')
                                else:
                                    esc2_2_1 = False
                                    newpage()
                                    print('이미 크리티컬 확률 최대레벨 입니다.\n')

                    # 크리티컬 돈 (2 -> 2 -> 2)
                    elif (n2_2 == 2):
                        esc2_2_2 = True
                        while esc2_2_2:
                            print(f"{coin}원 / 크리티컬 돈 : {cri_coin}%")
                            print(f"[ 비용 : {need_cri_coin}원 / 크리티컬 돈 : +{up_cri_coin}% ]")
                            print('\n1 : 업그레이드 / 2 : 취소\n')
                            n2_2_2 = in_put()
                            newpage()

                            # 크리티컬 돈 업글 (2 -> 2 -> 2 -> 1)
                            if (n2_2_2 == 1):
                                upgrade(need_cri_coin, 0, 0, 2.5, 2, n2, n2_2) # 크리티컬 돈 밸런스 (X, 비용)
                                
                            # 크리티컬 돈 나가기 (2 -> 2 -> 2 -> 2)
                            elif (n2_2_2 == 2):
                                esc2_2_2 = False
                            
                            # 잘못 입력 (2 -> 2 -> 2 -> ?)
                            else:
                                print('잘못 입력 하셨습니다.\n')
                    
                    # 크리티컬 나가기 (2 -> 2 -> 3)
                    elif (n2_2 == 3):
                        esc2_2 = False
                    
                    # 잘못 입력 (2 -> 2 -> ?)
                    else:
                        newpage()
                        print('잘못 입력 하셨습니다.\n')
            
            # 업그레이드 나가기 (2 -> 3)
            elif (n2 == 3):
                newpage()
                esc2 = False

            # 잘못 입력 (2 -> ?)
            else:
                newpage()
                print('잘못 입력 하셨습니다.\n')
    
    # 게임 종료 (3)
    elif (n == 3):
        break
    
    # 잘못 입력 (?)
    else:
        print('잘못 입력 하셨습니다.\n')

# 종료 멘트
newpage()
print(f"총 수익 : {coin}원")
print('제 게임을 플레이 해주셔서 감사합니다 :)')
print("Made By MiniGold649")
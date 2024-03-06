damage = 300

lvl = int(input("레벨 입력 : "))
moon = int(input("달 버프 (1:적용 / 2:취소) : "))
bk = int(input("균열 (1:적용 / 2:취소) : "))
cri = int(input("크리(%) : "))

cri /= 100
for i in range(1, lvl):
    damage += 10*i


if (moon == 2 and bk == 2):
    print(f"레벨 : {lvl} / 공격력 : {damage} / 크리적용 : {damage*cri}")
elif (moon == 1 and bk == 2):
    print(f"레벨 : {lvl} / 공격력 : {damage*1.7} / 크리적용 : {damage*cri*1.7}")
elif (moon == 2 and bk == 1):
    print(f"레벨 : {lvl} / 공격력 : {damage*2.524} / 크리적용 : {damage*cri*2.524}")
else:
    print(f"레벨 : {lvl} / 공격력 : {damage*2.524*1.7} / 크리적용 : {damage*cri*2.524*1.7}")
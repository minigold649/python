elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

print("\n"*20)
print("원소주기율표 맞추기!\n")

tri2 = True
while (tri2):
    tri = True
    while (tri):
        n = input("몇번째부터 맞추시겠습니까? (1 ~ 118)\n-> ")
        print("\n"*20)
        a = list(n)
        if (len(a) != 0):
            for i in range(len(a)):
                if (a[i] == '1' or a[i] == '2' or a[i] == '3' or a[i] == '4' or a[i] == '5' or a[i] == '6' or a[i] == '7' or a[i] == '8' or a[i] == '9' or a[i] == '0'):
                    tri = False
                    continue
                else:
                    print("잘못 입력\n")
                    tri = True
                    break
        else:
            print("잘못 입력\n")
    if (int(n) > 0 and int(n) < 119):
        tri2 = False
    else:
        print("잘못된 범위\n")

i = int(n)
no = 0
print("\n"*20)
while (i <= len(elements)):
    t = input(f"{i}번째 원소\n-> ")
    print("\n"*20)
    if (t == elements[i-1]):
        i += 1
    else:
        print("틀렸습니다.\n")
        no += 1

print("\n"*20)
print(f"시작위치 : {n}번째")
print(f"틀린횟수 : {no}개")
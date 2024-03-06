n = input("입력 ->")
#print(n)
a = list(n)
#print(a)
if (len(a) != 0):
    for i in range(len(a)):
        if (a[i] == '1' or a[i] == '2' or a[i] == '3' or a[i] == '4' or a[i] == '5' or a[i] == '6' or a[i] == '7' or a[i] == '8' or a[i] == '9' or a[i] == '0'):
            print("통과")
            continue
        else:
            print("숫자아님")
            break
else:
    print("숫자아님")
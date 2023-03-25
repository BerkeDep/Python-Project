import time
import decimal
a = int(input("karekökünü bulmak istediğiniz sayıyı giriniz: "))
c = int(input("virgüllü kısmın uzunluğunu giriniz: "))
c = c+2
print("tarama başlatılıyor")
decimal.getcontext().prec = c
rptnum = 0
count = 1
exit = 0
basamak = 0
ticket = 0
x = 0
while exit == 0:
    asama = "Aşama "+str(rptnum)
    print(asama)
    basamakare = 10**basamak
    add = decimal.Decimal(count) / decimal.Decimal(basamakare)
    while ((decimal.Decimal(x)+decimal.Decimal(add))**decimal.Decimal(2)) <= decimal.Decimal(a):
        x = decimal.Decimal(x) + decimal.Decimal(add)
        if (decimal.Decimal(x)*decimal.Decimal(x)) >= decimal.Decimal(a):
            if (decimal.Decimal(x)*decimal.Decimal(x)) == decimal.Decimal(a):
                print("girdiğiniz sayının karekökü: "+str(x))
                ticket = 1
                exit = 1
                break
            print("error")
            exit = 1
            break
    if len(str(x)) >= c:
        if ticket == 0:
            print("girdiğiniz sayının karekökü: "+str(x))
            break
    basamak += 1
    rptnum += 1
answer = str(input('sağlama yapmak için "1" yazınız: '))
answerExit = 0
if answer != str(1):
    answerExit = 1
if answerExit == 0:
    var1 = str(x).replace(".","")
    var2 = int(var1) ** 2
    varold = var2
    while decimal.Decimal(var2) > decimal.Decimal(x):
        var2 = decimal.Decimal(var2) / 10
    var2 = decimal.Decimal(var2) * 10
    print("Girdiğiniz sayının karesi:", var2)
    answerExit2 = 0
    answer2 = str(input('ham sonucu görmek için "1" yazınız'))
    if answer2 != str(1):
       answerExit2 = 1
    if answerExit2 == 0:
        print(varold)
input()
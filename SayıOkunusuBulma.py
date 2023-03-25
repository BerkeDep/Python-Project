sayi = int(input("sayi giriniz: "))

if sayi < 10 or sayi >= 100:
    print("girdiğiniz sayı 2 basamaklı olmalıdır")
else:
    OnlarBasamagı = sayi // 10
    BirlerBasamagı = sayi - (OnlarBasamagı*10)

    OnlarBasamagıOkunusu = ""
    BirlerBasamagıOkunusu = ""

    if OnlarBasamagı == 1:
        OnlarBasamagıOkunusu = "On"
    elif OnlarBasamagı == 2:
        OnlarBasamagıOkunusu = "Yirmi"
    elif OnlarBasamagı == 3:
        OnlarBasamagıOkunusu = "Otuz"
    elif OnlarBasamagı == 4:
        OnlarBasamagıOkunusu = "Kırk"
    elif OnlarBasamagı == 5:
        OnlarBasamagıOkunusu = "Elli"
    elif OnlarBasamagı == 6:
        OnlarBasamagıOkunusu = "Altmış"
    elif OnlarBasamagı == 7:
        OnlarBasamagıOkunusu = "Yetmiş"
    elif OnlarBasamagı == 8:
        OnlarBasamagıOkunusu = "Seksen"
    elif OnlarBasamagı == 9:
        OnlarBasamagıOkunusu = "Doksan"

    if BirlerBasamagı == 1:
        BirlerBasamagıOkunusu = "Bir"
    elif BirlerBasamagı == 2:
        BirlerBasamagıOkunusu = "İki"
    elif BirlerBasamagı == 3:
        BirlerBasamagıOkunusu = "Üç"
    elif BirlerBasamagı == 4:
        BirlerBasamagıOkunusu = "Dört"
    elif BirlerBasamagı == 5:
        BirlerBasamagıOkunusu = "Beş"
    elif BirlerBasamagı == 6:
        BirlerBasamagıOkunusu = "Altı"
    elif BirlerBasamagı == 7:
        BirlerBasamagıOkunusu = "Yedi"
    elif BirlerBasamagı == 8:
        BirlerBasamagıOkunusu = "Sekiz"
    elif BirlerBasamagı == 9:
        BirlerBasamagıOkunusu = "Dokuz"

    print(OnlarBasamagıOkunusu + " " + BirlerBasamagıOkunusu)
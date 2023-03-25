while True:
    sayi = int(input("Bir sayi giriniz: "))
    list = []
    def asalsayi(x):
        if sayi == 1:
            print("Bu sayı asal değildir")
        else:
            for i in range(2,sayi):
                if sayi % i == 0:
                    list.append(i)
            if list == []:
                print("Bu sayı asaldır")
            else:
                print("Bu sayı asal değildir")

    asalsayi(10)

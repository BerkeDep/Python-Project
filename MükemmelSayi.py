sayi = int(input("Sayi: "))
x = 1
bolenler = []
while sayi > x:
    if sayi % x == 0:
        bolenler.append(x)
    x += 1
LenBolenler = len(bolenler)
x = 0
toplam =0
while x < LenBolenler:
    toplam += bolenler[x]
    x+=1
print(bolenler)
print(toplam)
if toplam == sayi:
    print("Bu sayi bir mükemmel sayıdır")
else:
    print("Bu sayi bir mükemmel sayı değildir")



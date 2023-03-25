from mpmath import mp
import time
bul = int(input("aramak istediğin sayıları giriniz  "))
k = len(str(bul))
l = 10**k
x = l
print("tahmini basamak:", l)
while True:
    start = time.time()
    mp.dps = x
    print("hesaplanıyor...")
    pi = str(mp.pi)
    print("hesaplandı!")
    print("arama başlatıldı")
    a = pi.find(str(bul))
    if a >= 0:
        print("bulundu!")
        print("dosyaya yazma başlatılıyor...")
        file = open("pi.txt","a+")
        file.close()
        file = open("pi.txt", "w+")
        file.write(str(pi))
        file.close()
        print("dosyaya yazma işlemi bitti!")
        print(a)
        end = time.time()
        m = end - start
        print("hesaplama:", int(m), "saniye sürdü")
        y = input()
        quit()
    else:
        print(x)
        x += 1000


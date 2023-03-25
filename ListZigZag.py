import time
uzunluk = int(input("uzunluk giriniz: "))
wt = float(input("bekleme süresi giriniz: "))
add = input("değişkeni giriniz: ")
adds = input("sabiti giriniz: ")
if uzunluk == 1:
    print("uzunluk 1 olamaz")
    exit()
a = []
def getA():
    global a
    x = 0
    a = []
    while (uzunluk-1) > x:
        a.append(adds)
        x += 1

while True:
    x = 0
    getA()
    while x <= (len(a)-1):
        getA()
        a.insert(x, add)
        time.sleep(wt)
        print(a)
        x += 1
        if x > (len(a)-2):
            while x >= 0:
                getA()
                a.insert(x, add)
                time.sleep(wt)
                print(a)
                x -= 1
                if x < 1:
                    break
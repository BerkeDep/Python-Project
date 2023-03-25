a = 1
b = 1
fibonacci = [a,b]
sayi = int(input("bulmak istediğiniz basamağı giriniz: "))
for i in range(sayi - 2):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci[(len(fibonacci)-1)])

max = int(input("Maksimum değeri giriniz: "))
x = 1
y = 1
z = 1
def kntrl(a,b,c):
    if (a**2) + (b**2) == (c**2):
        txt = str(a) + " " + str(b) + " " + str(c)
        return txt
x = 1
while x < max:
    if kntrl(x,y,z) != None and y < x:
        print(kntrl(x,y,z))
    y = 1
    while y < max:
        if kntrl(x, y, z) != None and y < x:
            print(kntrl(x, y, z))
        z = 1
        while z < max:
            if kntrl(x, y, z) != None and y < x:
                print(kntrl(x, y, z))
            z += 1
        y += 1
    x += 1
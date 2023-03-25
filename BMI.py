boy = int(input("Boyunuzu giriniz(cm): "))
boy = boy / 100
kilo = int(input("Kilonuzu giriniz(kg): "))
BMI = kilo / (boy**2)
if BMI < 18.5:
    print("Zayıf")
elif BMI >= 18.5 and BMI < 25:
    print("Normal")
elif BMI >= 25 and BMI < 30:
    print("Fazla kilolu")
elif BMI > 30:
    print("Obez")
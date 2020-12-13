__author__="merv"
while True:
    print ("Dörtgen (1)")
    print("Üçgen (2)")
    sekil= input("Hangi şeklin tipini öğrenmek istiyorsun:")

    if (sekil=="1"):
        print("Lütfen kenarları sırası ile giriniz..")
        a =  int(input("1. kenar"))
        b = int(input("2. kenar"))
        c = int(input("3. kenar"))
        d = int(input("4. kenar"))
        if((a==0) or (b==0) or (c==0) or (d==0)):
            print("geçersiz kenar girdiniz")
        if(a==b and a==c and a==d):
            print("Kare")
        elif( a==c and b==d):
            print("Dikdörtgen")
        else:
            print("dörtgen")
    elif (sekil=="2"):
        a= int(input("1. kenar"))
        b = int(input("2. kenar"))
        c = int(input("3. kenar"))
        if(abs(a+b)>c, abs(a+c)>b,abs(b+c)>a):
            print("geçersiz kenar girdiniz")
            if(a==b and a==c):
                print("Eşkenar üçgen")
            elif(a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
                print("ikizkenar üçgen")
            else:
                print("çeşitkenar üçgen")
        else:
            print("üçgen belirtmiyor")
    else:
        print("Geçersiz şekil girdiniz...")
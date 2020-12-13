#girilen sayı 100 den küçükse sayının 5 ile bölümünden kalan, büyükse 7 ile böl

"""sayi= int(input("sayi giriniz:"))
if (sayi<100):
    print(sayi %5)
else:
    print(sayi %7)


#kullanıcının girdiği 3sayı topla, sonucu 50den büyükse toplamın 2 katını al, küçükse toplamın karesi

a= int(input("1. sayi giriniz:"))
b= int(input("2. sayi giriniz:"))
c= int(input("3. sayi giriniz:"))

toplam = a + b + c
if (toplam >50):
    print(toplam*2)
else:
    print(toplam**2)

#girilen sayi 0 ile 10 arasında ise girdiğiniz sayi 0 ile 50 arasındadır yazacak değilse

x=int(input("bir sayi giriniz:"))
if (0<=x<=10):            #if x>0 and x<10: şeklinde de yazılabilir.
    print("sayiniz 0 ile 10 arasında")
elif (10<x<20):
    print(("sayiniz 10 ile 20 arasında"))
elif x>20 and x<30:
    print(("sayiniz 20 ile 30 arasında"))
elif x>30 and x<40:
    print("sayiniz 30 ile 40 arasında")
elif x>40 and x<50:
    print("sayiniz 40 ile 50 arasında")
else:
    print("sayiniz 0 ile 50 arasında değil")"""

#vize notlarını girdir vizenin &40 finalin %60
vize1= float(input("1. vize notunu giriniz:"))
final= float(input("Final notunu giriniz:"))
ortalama= vize1*0.4+final*0.6
print(ortalama)
if vize1==58 or final==58:
    print("geçtiniz")
else:
    if  ortalama>0 and ortalama<50 :
         print("kaldınız")
    elif ortalama>50 and ortalama<85:
        print("iyisin")
    elif ortalama>85 and ortalama<100:
         print("helal olsun")
    elif vize1==58  or final==58:
         print("geçtiniz")


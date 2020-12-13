print ("""*******************************
Hesap Makinesi Programı
İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
****************************
""")

a= int(input("Birinci sayıyı giriniz:"))
b= int(input(" İkinci sayıyı giriniz:"))
islem= input("İşlemi giriniz:")


if islem=="1":
    print("{} ile  {} in toplamı {} dır.". format (a,b,a+b))
elif islem=="2":
    print(" {}ile {} nin farkı {} dır".format (a,b,a-b))
elif islem=="3":
    print("{} ile {} nin çarpımı {} dır".format (a,b,a*b))
elif islem== "4":
    print("{} ile {}nin bölmümü {}dır".format (a,b,a/b))
else:
    print("Doğru bir işlem girmediniz..")
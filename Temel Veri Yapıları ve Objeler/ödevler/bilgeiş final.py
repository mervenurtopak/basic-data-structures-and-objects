__author__= "BilgeIş Proje"
while True:
    print("0-50 arasında (1)")
    print("50-70 arasında (2)")
    print("70-85 arasında (3)")
    print("85-1000 arasında (4)")
    print
    secim = input("Puanınız hangi aralıkta...:")
    isim = input("isminiz:")

    if secim=="1":
        print("Kaldınız",isim)
        print
    elif secim=="2":
        print("Orta not",isim)
        print
    elif secim=="3":
        print("İyi not",isim)
        print
    elif secim=="4":
        print("Çok iyi not",isim)
        print
    else:
        print("Geçersiz not girdiniz... Program sonlandırılıyor")
        break
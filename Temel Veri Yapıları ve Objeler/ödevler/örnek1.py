__author__="merv"
while True:
    print ("Sabah (1)")
    print("Öğle (2)")
    print ("Akşam (3)")
    print("Gece (4)")
    secim= input ("gün içerisindeki zaman dilimini giriniz....")
    isim= input(("isminiz:"))

    if secim=="1":
      print("Günaydın" , isim)
      print
    elif secim=="2":
      print("Tünaydın",isim)
      print
    elif secim=="3":
      print("İyi akşamlar",isim)
      print
    elif secim=="4":
      print("İyi geceler",isim)
      print
    else:
      print("Gün aralığı geçersiz.. Program sonlandırılıyor..")
    break
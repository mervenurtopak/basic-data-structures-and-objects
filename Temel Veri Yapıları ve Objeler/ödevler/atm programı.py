print("""
*************
Atm Makinesine Hoşgeldiniz...
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için "q"ya basın
*************
""")
bakiye=1000
while True:
    islem= input("Yapmak istediğiniz işlemi seçiniz:")
    if islem=="q":
        print("Yine Bekleriz...")
        break
    elif islem=="1":
        print("Bakiyeniz{} Tl dir".format(bakiye))
    elif islem=="2":
        miktar=int(input("Yatırmak istediğiniz miktarı giriniz:"))
        bakiye+=miktar
        print("Yeni Bakiyeniz:{}".format(bakiye))
    elif islem=="3":
        miktar=int(input("Çekmek istediğiniz miktarı giriniz"))
        if miktar>bakiye:
            print("Böyle bir miktar çekemezsiniz")
            continue
        bakiye-=miktar
        print("Kalan bakiyeniz:{}".format(bakiye))
    else:
        print("Geçersiz işlem girdiniz")
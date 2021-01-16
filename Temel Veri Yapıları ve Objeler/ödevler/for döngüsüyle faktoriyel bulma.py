print("""
************
Faktoriyel Bulma
Çıkış yapmak için "q"ya basınız
*************
""")
while True:
    sayi=(input("Faktoriyelini almak istediğiniz sayıyı giriniz:"))
    if sayi=="q":
        print("Programdan çıkılıyor...")
        break
    else:
        sayi=int(sayi)
        faktoriyel=1
        for i in range(2,sayi+1):
            faktoriyel*= i
        print("faktoriyel:",faktoriyel,"sayı:",i)


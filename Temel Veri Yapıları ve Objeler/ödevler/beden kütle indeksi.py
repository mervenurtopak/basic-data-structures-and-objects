print("""*******************
BEDEN KÜTLE İNDEKSİ
*******************""")

kilo=int (input("Kilonuzu kg cinsinden giriniz:"))
boy= float(input("Boyunuzu metre cinsinden giriniz:"))
beden_kitle_indeksi= kilo/boy**2

if (beden_kitle_indeksi<18.5):
    print("Zayıf")
elif (beden_kitle_indeksi>18.5 and beden_kitle_indeksi<25):
    print("Normal...")
elif (beden_kitle_indeksi>25 and beden_kitle_indeksi<30):
    print("Fazla kilolu")
else:
    print("Obez")

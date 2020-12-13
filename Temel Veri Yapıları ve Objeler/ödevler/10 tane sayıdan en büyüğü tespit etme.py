i=0
sayi1=int(input("Sayi giriniz: "))
enbuyuk=sayi1
while i<9:
    sayi2=int(input("Sayi giriniz: "))
    if sayi2>enbuyuk:
        enbuyuk=sayi2
    i=i+1
print(enbuyuk)
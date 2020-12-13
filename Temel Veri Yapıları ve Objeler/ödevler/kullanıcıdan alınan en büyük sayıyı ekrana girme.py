a= int(input("1. sayıyı giriniz:"))
b= int(input("2. sayıyı giriniz:"))
c= int(input("3. Sayıyı giriniz:"))

if(a>=b and a >=c):
    print("En büyük sayı:",a)
elif (b>=a and b>=c):
    print("En büyük sayı:",b)
else:
    print("En büyük sayı:",c)
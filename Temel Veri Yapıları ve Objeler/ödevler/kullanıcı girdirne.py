print("""*******************
Kullanıcı Girişi
*******************
""")

sys_kullanici_adi = "merv"
sys_parola = "12345"

kullanici_adi= input("Kullanıcı adı:")
parola= input("Parola:")

if (sys_kullanici_adi==kullanici_adi and sys_parola!=parola):
    print("Parola Yanlış...")
elif (sys_kullanici_adi != kullanici_adi and sys_parola==parola):
    print("Kullanıcı adı yanlış...")
elif (sys_parola != parola and sys_kullanici_adi != kullanici_adi):
    print("Kullanıcı adı ve şifre yanlış...")
else:
    print("Sisteme giriş yapılıyor...")
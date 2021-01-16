print("""
Kullanıcı Girişi Programı..
""")

sys_kullanici_adi="merv"
sys_sifre="12345"
giris_hakki=3

while True:
    kullanici_adi= input("Kullanıcı adı:")
    sifre= input("Şifre:")
    if sys_kullanici_adi==kullanici_adi and sifre!=sys_sifre:
        print("Şifre Hatalı...")
        giris_hakki-=1
    elif sys_kullanici_adi!=kullanici_adi and sifre==sys_sifre:
        print("Kullanıcı Adı Hatalı...")
        giris_hakki-=1
    elif sys_kullanici_adi!=kullanici_adi and sifre!=sys_sifre:
        print("Kullanıcı adı ve şifre hatalı")
        giris_hakki-=1
    else:
        print("Sisteme başarıyla giriş yapılıyor...")
        break
    if giris_hakki==0:
        print("Giriş hakkınız doldu")
        break
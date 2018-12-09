bilgiler = []



def kaydol():
    ad = input("Kullanıcı adı giriniz: ")
    if (ad in bilgiler):
        print("Bu kullanıcı adı zaten kayıtlıdır.")
        bilgiler.append(ad)
    else:
        şifre = input("Şifre giriniz.")
        bilgiler.append(şifre)


        return bilgiler


def giriş():

    doğrulama = input("Bot musunuz ?")


    ad = input("Kullanıcı adı giriniz: ")
    şifre = input("Şifreyi giriniz: ")


    if (ad and şifre in bilgiler and doğrulama == "hayır"):

        print("Giriş başarılı.")
    else:
        print("Bilgileriniz veya recaptcha doğrulamanız yanlış. Tekrar deneyiniz.")


def çıkış():

    while True:
        çıkış = input("Çıkış yapmak istiyor musunuz ?")

        if(çıkış == "evet"):
            print("Sistemden çıkılıyor..")
            break
        else:
            print("Eksik tuşlama yaptınız..")




print("""

***********************************      
İŞLEMLER;

-kaydol

-giriş (Burada recaptcha doğrulaması vardır. "hayır" ile yanıt vermeyen kullanıcılar sistemden atılacaktır.)

-çıkış
************************************
""")

while True:
    işlem = input("İşlem seçiniz: ")

    if (işlem == "kaydol"):
        kaydol()
    if (işlem == "giriş"):
        giriş()
    if (işlem == "çıkış"):
        çıkış()
        break


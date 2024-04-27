import time
import os
import json

with open("kullanicilar.json", "r") as dosya:
    kullanicilar_dict = json.load(dosya)

print("Sisteme giriş yapabilmek için lütfen kullanıcı adınızı ve şifrenizi giriniz.")
print("Kayıt olmak için 'reg' ya da 'register' yazın.")

while True:
    giris_isim = input("Kullanıcı adınızı girin: ")

    if giris_isim == "reg" or giris_isim == "register":
        yeni_kullanici_adı = input("Yeni kullanıcı adınızı girin: ")
        if yeni_kullanici_adı in kullanicilar_dict:
            print("Bu kullanıcı adı zaten kullanımda. Lütfen başka bir kullanıcı adı seçin.")
            continue

        yeni_sifre = input("Yeni şifrenizi girin: ")

        # Yeni kullanıcıyı ekle
        kullanicilar_dict[yeni_kullanici_adı] = yeni_sifre

        # Kullanıcıları güncellenmiş haliyle dosyaya yaz
        with open("kullanicilar.json", "w") as dosya:
            json.dump(kullanicilar_dict, dosya)
        print("Kayıt başarılı. Lütfen giriş yapın.")
    elif giris_isim in kullanicilar_dict:
        print("Kullanıcı adı kontrol ediliyor...")
        time.sleep(1)
        print("Onaylandı.")

        giris_sifre = input("Şifrenizi girin: ")

        while giris_sifre != kullanicilar_dict[giris_isim]:
            print("Şifre doğru değil. Lütfen tekrar deneyin.")
            giris_sifre = input("Şifrenizi girin: ")

        print("Şifre kontrol ediliyor...")
        time.sleep(1)
        print("Şifre doğrulandı.")
        #...
        time.sleep(0.5)
        print("...")
        print("Program 10sn sonra kapanacak.")
        time.sleep(10)
        #...burayı sılıp kendı kodlarınızı yazabılırsınız.
        break
    else:
        print("Kullanıcı adınız doğru değil. Lütfen tekrar deneyin.")

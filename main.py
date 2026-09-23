# Denenecek tüm karakterler (rakamlar)
karakterler = "0123456789"

# Doğru şifre (kullanıcıdan alınan)
dogru_sifre = input("🔐 Şifreni yaz (örnek: 123): ")

# Deneme sayısı
deneme_sayisi = 0

# 3 haneli tüm kombinasyonları dene
for birinci in karakterler:
    for ikinci in karakterler:
        for ucuncu in karakterler:
            tahmin = birinci + ikinci + ucuncu
            deneme_sayisi += 1
            print(f"{deneme_sayisi}. Deneme: {tahmin}")
            
            if tahmin == dogru_sifre:
                print(f"✅ Şifre bulundu: {tahmin}")
                print(f"🔢 Toplam deneme: {deneme_sayisi}")
                exit()

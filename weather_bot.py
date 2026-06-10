import urllib.request
import urllib.parse  # Yeni: Türkçe karakterleri internet diline çevirmek için
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

print("="*50)
print("🌍 SÜPER AKILLI COĞRAFİ HAVA DURUMU BOTU v4.0 🌍")
print("="*50)
print("Sadece 81 il değil, dünya üzerindeki her yeri arayabilirsiniz!")
print("Çıkmak için 'q' yazın.\n")

while True:
    # Kullanıcıdan şehir veya ilçe ismini alıyoruz
    secilen_sehir = input("Şehir veya İlçe ismi girin: ").strip()
    
    if secilen_sehir.lower() == 'q':
        print("\nSistem kapatılıyor. Güvenli günler dileriz!")
        break
        
    if not secilen_sehir:
        continue

    print(f"-> {secilen_sehir.upper()} aranıyor...")
    
    try:
        # 1. ADIM: Şehir ismini URL formatına güvenli bir şekilde çeviriyoruz (Örn: 'izmir' -> 'izmir')
        sehir_kodlu = urllib.parse.quote(secilen_sehir)
        
        # Coğrafi Konum Bulucu API adresi (Geocoding)
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={sehir_kodlu}&count=1&language=tr&format=json"
        
        maske_baslik = {'User-Agent': 'Mozilla/5.0'}
        geo_istek = urllib.request.Request(geo_url, headers=maske_baslik)
        geo_baglanti = urllib.request.urlopen(geo_istek)
        geo_veri = json.loads(geo_baglanti.read())
        
        # Eğer girilen isim dünyada hiçbir yerle eşleşmediyse sonuç boş döner
        if "results" not in geo_veri or not geo_veri["results"]:
            print(f"❌ '{secilen_sehir}' adında bir yer bulunamadı! Lütfen tekrar deneyin.\n")
            continue
            
        # API'den gelen ilk sonucun koordinatlarını ve resmi adını cımbızla çekiyoruz
        enlem = geo_veri["results"][0]["latitude"]
        boylam = geo_veri["results"][0]["longitude"]
        tam_ad = geo_veri["results"][0]["name"]
        ulke = geo_veri["results"][0].get("country", "Bilinmiyor")
        
        # 2. ADIM: Bulduğumuz bu koordinatları otomatik olarak hava durumu API'sine paslıyoruz
        hava_url = f"https://api.open-meteo.com/v1/forecast?latitude={enlem}&longitude={boylam}&current_weather=true"
        
        hava_istek = urllib.request.Request(hava_url, headers=maske_baslik)
        hava_baglanti = urllib.request.urlopen(hava_istek)
        hava_veri = json.loads(hava_baglanti.read())
        
        anlik_durum = hava_veri["current_weather"]
        sicaklik = anlik_durum["temperature"]
        ruzgar_hizi = anlik_durum["windspeed"]
        
        # Sonuçları ekrana basıyoruz
        print("-" * 35)
        print(f"📍 Bulunan Konum : {tam_ad} ({ulke})")
        print(f"🌡️ Anlık Sıcaklık : {sicaklik}°C")
        print(f"💨 Rüzgar Hızı   : {ruzgar_hizi} km/s")
        print("-" * 35 + "\n")
        
    except Exception as e:
        print("⚠️ Bağlantı sırasında bir hata oluştu, lütfen tekrar deneyin.\n")
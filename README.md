# 🌍 Coğrafi Hava Durumu Botu (Geocoding & Weather CLI)

Bu proje, kullanıcının girdiği şehir veya ilçe ismini dinamik olarak coğrafi koordinatlara çeviren ve ardından bu koordinatları kullanarak anlık hava durumu verilerini çeken **kesintisiz (continuous) bir CLI aracıdır**.

Projede iki farklı açık kaynaklı API birbirine zincirlenerek (**API Chaining**) statik veri tabanı zorunluluğu ortadan kaldırılmış ve dünya genelinde arama desteği sağlanmıştır.

## 🚀 Özellikler

* **Küresel Arama Desteği:** Sadece Türkiye'nin 81 ili değil, dünya üzerindeki tüm şehir ve ilçeler için arama yapabilir.
* **API Zincirleme (API Chaining):** `Open-Meteo Geocoding API` üzerinden alınan enlem/boylam verileri, anlık olarak `Weather Forecast API`ye paslanır.
* **Güvenlik Duvarı Bypass (User-Agent Masking):** Sunucu taraflı bot engellemelerini (HTTP 403 Forbidden) aşmak için tarayıcı simülasyonu (Header Masking) kullanılmıştır.
* **Kesintisiz Döngü (Continuous Session):** `while True` mimarisi sayesinde kullanıcı 'q' tuşuna basana kadar uygulama kapanmadan yeni sorgular kabul eder.
* **Hata Yönetimi (Exception Handling):** Geçersiz konum girişlerinde veya ağ kopmalarında uygulamanın çökmesini engelleyen `try-except` blokları mevcuttur.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.13+
* **Kütüphaneler:** * `urllib.request` & `urllib.parse` (Ağ istekleri ve URL kodlama)
  * `json` (Veri ayrıştırma / JSON parsing)
  * `ssl` (Yerel sertifika doğrulama yönetimi)


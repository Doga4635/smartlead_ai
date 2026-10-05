# Smartlead AI - AI Supported Lead Management & Chatbot Platform

Bu proje, **Wix** tabanlı ön yüz ile entegre çalışan; kullanıcı etkileşimlerini (lead kayıtları) veritabanına kaydeden ve **Groq API** destekli yapay zekâ kariyer danışmanı sunan **Flask** tabanlı bir backend servisidir.

---

## 🚀 Özellikler

* **AI Danışman Chatbot:** Groq API altyapısı ile kullanıcı sorularını yanıtlar, sohbet geçmişini korur.
* **Lead Kaydetme & Yönetimi:** Web sitesi üzerinden gelen kullanıcı iletişim bilgilerini SQLite veritabanına kaydeder.
* **Yönetici Paneli (Dashboard):** Gelen potansiyel müşteri kayıtlarını (lead) liste halinde görüntüleme imkanı sağlar.
* **Esnek ve Güvenli Mimari:** Modüler servis yapısı, CORS desteği ve API anahtarı güvenliği için `.env` yapılandırması.

---

## 🛠️ Teknolojiler

* **Backend:** Python, Flask
* **AI Integration:** Groq API
* **Frontend Entegrasyonu:** Wix Velo
* **Veritabanı:** SQLite

---

## 📦 Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın
```bash
git clone [https://github.com/kullanici-adiniz/proje-adi.git](https://github.com/kullanici-adiniz/proje-adi.git)
cd proje-adi
```

### 2. Sanal Ortamı Oluşturun ve Aktifleştirin
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4. .env Dosyasını Oluşturun
Proje kök dizininde .env adında bir dosya oluşturun ve içeriğini düzenleyin:
```bash
GROQ_API_KEY=gsk_sizin_gercek_groq_api_anahtariniz
BUSINESS_CONTEXT=Ben AI asistanıyım...
```

### 5. Uygulamayı Çalıştırın
```bash
python run.py
```
Uygulama varsayılan olarak http://127.0.0.1:5000 adresinde çalışacaktır.

🔌 API Endpoint'leri
✅ POST /api/leads -> Yeni lead (iletişim bilgisi) kaydeder.

✅ POST /api/sohbet -> Kullanıcı mesajını alır, sohbet geçmişiyle birlikte AI servisine gönderir ve yanıt döner.

✅ GET /dashboard -> Kayıtlı lead listesini gösteren yönetim panelidir.







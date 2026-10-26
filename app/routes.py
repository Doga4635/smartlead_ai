from flask import Blueprint, render_template, request, jsonify
from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError
from config import get_config

pages_bp = Blueprint('pages', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')

config = get_config()


# ==========================================
# SAYFA ROTALARI (PAGES BLUEPRINT)
# ==========================================

@pages_bp.route('/', methods=['GET'])
def index():
    """Ziyaretçilerin AI ile sohbet ettiği karşılama sayfası."""
    return render_template('index.html')


@pages_bp.route('/dashboard', methods=['GET'])
def dashboard():
    """İşletme sahibinin kayıtlı lead'leri gördüğü yönetim paneli."""
    # Lead verileri bu sayfada değil, panelin çağırdığı korumalı API üzerinden yüklenir.
    return render_template('dashboard.html')


# ==========================================
# API ROTALARI (API BLUEPRINT - /api)
# ==========================================

@api_bp.route('/sohbet', methods=['POST'])
def sohbet():
    """
    Kullanıcı mesajını ve geçmişini alır, AI servisine iletir.
    Örnek Body: {"mesaj": "Merhaba", "gecmis": [...]}
    """
    data = request.get_json() or {}
    # Mesaj geçmişi isteğe bağlıdır; servis yeni sohbeti boş geçmişle başlatabilir.
    mesaj = data.get('mesaj')
    gecmis = data.get('gecmis', [])

    # Validation: Eksik veri kontrolü
    if not mesaj or not str(mesaj).strip():
        return jsonify({
            'basari': False,
            'hata': "Mesaj alanı boş bırakılamaz."
        }), 400

    try:
        # AI Servis Katmanına Yönlendirme
        yanit = ai_service.yanit_uret(mesaj=mesaj, gecmis=gecmis)
        return jsonify({
            'basari': True,
            'yanit': yanit
        }), 200

    # app/routes.py içindeki sohbet fonksiyonu
    except AIServiceError as e:
        # Dış AI sağlayıcısına özgü hatalar geçici servis kullanılamıyor yanıtına çevrilir.
        return jsonify({
        'basari': False,
        'hata': f"AI Servis Hatası: {str(e)}"  # Gerçek iç hatayı yanıta ekliyoruz
    }), 503

    except Exception as e:
        # Beklenmeyen dahili hataların ayrıntılarını istemciye sızdırmadan genel hata döndürür.
        return jsonify({
            'basari': False,
            'hata': "Sunucu tarafında beklenmeyen bir hata oluştu."
        }), 500


@api_bp.route('/leads', methods=['POST'])
def yeni_lead():
    """
    Yeni müşteri adayı (lead) kaydeder.
    Örnek Body: {
        "isim": "Ahmet Yılmaz",
        "telefon": "05551112233",
        "email": "ahmet@example.com",
        "meslek": "Öğrenci",
        "kariyer_hedefi": "UI/UX Tasarımı",
        "haftalik_zaman": "10-15 saat",
        "mesaj": "Eğitim programı hakkında bilgi almak istiyorum."
    }
    """
    data = request.get_json() or {}
    
    # Kayıt oluşturulmadan önce API sözleşmesindeki zorunlu iletişim alanlarını doğrular.
    isim = data.get('isim')
    telefon = data.get('telefon')
    email = data.get('email')
    
    # Zorunlu alan kontrolü
    if not isim or not telefon or not email:
        return jsonify({
            'basari': False,
            'hata': "İsim, telefon ve e-posta alanları zorunludur."
        }), 400

    try:
        # Veritabanı Katmanına Yönlendirme
        lead_id = lead_ekle(
            isim=isim,
            telefon=telefon,
            email=email,
            meslek=data.get('meslek'),
            kariyer_hedefi=data.get('kariyer_hedefi'),
            haftalik_zaman=data.get('haftalik_zaman'),
            mesaj=data.get('mesaj')
        )

        return jsonify({
            'basari': True,
            'mesaj': "Kayıt başarıyla oluşturuldu.",
            'lead_id': lead_id
        }), 201

    except Exception as e:
        # Veritabanı/işlem hatalarında kayıt başarılıymış gibi yanıt vermemek için 500 döner.
        return jsonify({
            'basari': False,
            'hata': "Lead kaydı oluşturulurken bir hata oluştu."
        }), 500


@api_bp.route('/leads', methods=['GET'])
def leads_listele():
    # Panelin gönderdiği yönetici parolasını veritabanı sorgusundan önce doğrular.
    gelen_sifre = request.headers.get('X-Admin-Password')
    
    if not gelen_sifre or gelen_sifre != config.ADMIN_PASSWORD:
        return jsonify({
            'basari': False,
            'hata': 'Yetkisiz erişim! Geçersiz admin şifresi.'
        }), 401
    
    try:
        # Yetkilendirme başarılıysa kayıtları alıp toplam sayısıyla birlikte JSON olarak döndürür.
        veriler = tum_leadler()
        return jsonify({
            'basari': True,
            'toplam': len(veriler),
            'veri': veriler
        }), 200
    except Exception as e:
        return jsonify({
            'basari': False,
            'hata': 'Veriler çekilirken bir hata oluştu.'
        }), 500
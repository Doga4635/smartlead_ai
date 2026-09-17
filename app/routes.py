from flask import Blueprint, render_template, request, jsonify

# app/ database.py içinden
from app.database import lead_ekle, tum_leadler

# app/services/ai_service.py içinden
from app.services.ai_service import ai_service, AIServiceError

pages_bp = Blueprint('pages', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')


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

    except AIServiceError as e:
        # AI Servisi hatası durumunda 503 Service Unavailable
        return jsonify({
            'basari': False,
            'hata': "Şu anda yapay zekâ servisine ulaşılamıyor. Lütfen biraz sonra tekrar deneyin.",
            'detay': str(e)
        }), 503

    except Exception as e:
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
        return jsonify({
            'basari': False,
            'hata': "Lead kaydı oluşturulurken bir hata oluştu."
        }), 500


@api_bp.route('/leads', methods=['GET'])
def lead_listesi():
    """Tüm lead kayıtlarını veritabanından çekip liste olarak döndürür."""
    try:
        # Veritabanı Katmanına Yönlendirme
        leads = tum_leadler()
        return jsonify({
            'basari': True,
            'veri': leads,
            'toplam': len(leads)
        }), 200

    except Exception as e:
        return jsonify({
            'basari': False,
            'hata': "Kayıtlar çekilirken bir hata oluştu."
        }), 500
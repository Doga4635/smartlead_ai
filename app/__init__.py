from flask import Flask, jsonify
from flask_cors import CORS

# Kök dizindeki config.py'den alıyoruz
from config import get_config 

# app/ klasörü içindeki modüllerden alıyoruz
from app.database import init_db
from app.routes import pages_bp, api_bp

def create_app():
    # Flask uygulamasını oluşturup ayarları ve bağımlı bileşenleri tek yerde bağlar.
    app = Flask(__name__)
    
    config_class = get_config()
    app.config.from_object(config_class)
    
    # Tarayıcıların farklı kökenlerden gelen yanıtlara erişimini yapılandırmadaki CORS listesine göre sınırlar.
    CORS(app, resources={r"/*": {"origins": app.config.get('CORS_ORIGINS', '*')}})
    
    # İstekler başlamadan önce veritabanı şemasının hazır olmasını sağlar.
    with app.app_context():
        init_db(app)
        
    # Sayfa ve API adreslerini ilgili blueprint'lere yönlendirir.
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)
    
    @app.route('/health', methods=['GET'])
    def health_check():
        # Dağıtım araçlarının servisin ayakta olup olmadığını kontrol edebilmesi için basit yanıt verir.
        return jsonify({
            'durum': 'canli',
            'mesaj': 'SmartLead AI / Callifex servisi sorunsuz çalışıyor.'
        }), 200

    return app
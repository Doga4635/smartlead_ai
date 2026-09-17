from flask import Flask, jsonify
from flask_cors import CORS

# Kök dizindeki config.py'den alıyoruz
from config import get_config 

# app/ klasörü içindeki modüllerden alıyoruz
from app.database import init_db
from app.routes import pages_bp, api_bp

def create_app():
    app = Flask(__name__)
    
    config_class = get_config()
    app.config.from_object(config_class)
    
    CORS(app, resources={r"/*": {"origins": app.config.get('CORS_ORIGINS', '*')}})
    
    with app.app_context():
        init_db(app)
        
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)
    
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({
            'durum': 'canli',
            'mesaj': 'SmartLead AI / Callifex servisi sorunsuz çalışıyor.'
        }), 200

    return app
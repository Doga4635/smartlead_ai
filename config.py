import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri os.environ içerisine yükler
load_dotenv()

class Config:
    """Temel yapılandırma sınıfı."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-secret-key')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///smartlead.db')
    
    # AI Yapılandırması
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    BUSINESS_CONTEXT = os.environ.get(
        'BUSINESS_CONTEXT',
        'Sen bir yapay zekâ asistanısın. Ziyaretçilere yardımcı ol ve iletişim bilgilerini topla.'
    )
    
    # Güvenlik ve Ağ
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')

class DevelopmentConfig(Config):
    """Geliştirme ortamı ayarları."""
    DEBUG = True

class ProductionConfig(Config):
    """Üretim (Canlı) ortamı ayarları."""
    DEBUG = False
    # Canlı ortamda SECRET_KEY varsayılan kalmasın uyarısı/kontrolü eklenebilir

# Ortam seçimi için sözlük yapısı
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config():
    """FLASK_ENV değişkenine göre ilgili config sınıfını döndürür."""
    env = os.environ.get('FLASK_ENV', 'default')
    return config_by_name.get(env, DevelopmentConfig)
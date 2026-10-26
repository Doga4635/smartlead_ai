import os
from dotenv import load_dotenv

# Yerel geliştirme ayarlarının da ortam değişkenleri gibi okunabilmesi için .env dosyasını yükler.
load_dotenv()

class Config:
    """Temel yapılandırma sınıfı."""
    # Ortam değişkenleri varsa önceliklidir; yoksa yerel geliştirme varsayılanları kullanılır.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-secret-key')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///smartlead.db')
    
    # AI Yapılandırması
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "varsayilan_admin_sifre") # Admin şifresi
    BUSINESS_CONTEXT = os.environ.get(
        'BUSINESS_CONTEXT',
        'Sen bir yapay zekâ asistanısın. Ziyaretçilere yardımcı ol ve iletişim bilgilerini topla.'
    )
    
    # Güvenlik ve Ağ
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')
    

# FLASK_ENV değerlerini yapılandırma sınıflarına eşler; tanınmayan değerler Config'e düşer.
config_by_name = {
    'default': Config
}

def get_config():
    """FLASK_ENV değişkenine göre ilgili config sınıfını döndürür."""
    # Ortam belirtilmemişse veya eşleşen bir sınıf yoksa temel yapılandırma kullanılır.
    env = os.environ.get('FLASK_ENV', 'default')
    return config_by_name.get(env, Config)
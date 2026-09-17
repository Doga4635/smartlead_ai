import sqlite3
from config import get_config

def get_db():
    """
    Veritabanına bağlanır ve sütun adlarına isimle (row['isim'] gibi) 
    erişebilmek için row_factory ayarını yapar.
    """
    config = get_config()
    # SQLite URL formatı: sqlite:///smartlead.db -> dosya adını ayıklıyoruz
    db_path = config.DATABASE_URL.replace('sqlite:///', '')
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Sözlük benzeri sütun erişimi sağlar
    return conn

def init_db(app=None):
    """
    'leads' tablosunu oluşturur (yoksa).
    Flask app nesnesi verilirse uygulama bağlamı (context) ile çağrılabilir.
    """
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            telefon TEXT NOT NULL,
            email TEXT NOT NULL,
            meslek TEXT,
            kariyer_hedefi TEXT,
            haftalik_zaman TEXT,
            mesaj TEXT,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def lead_ekle(isim, telefon, email, meslek=None, kariyer_hedefi=None, haftalik_zaman=None, mesaj=None):
    """
    Yeni bir müşteri adayı (lead) kaydı ekler.
    SQL Injection koruması için yer tutucu (?) parametreleri kullanılmıştır.
    """
    conn = get_db()
    cursor = conn.cursor()
    
    query = '''
        INSERT INTO leads (isim, telefon, email, meslek, kariyer_hedefi, haftalik_zaman, mesaj)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    
    cursor.execute(query, (isim, telefon, email, meslek, kariyer_hedefi, haftalik_zaman, mesaj))
    conn.commit()
    
    new_id = cursor.lastrowid
    conn.close()
    
    return new_id

def tum_leadler():
    """
    Tüm müşteri adayı kayıtlarını en yeniden eskiye doğru getirir.
    Dönen sonuçlar sözlük (dict) formatına dönüştürülür.
    """
    conn = get_db()
    cursor = conn.cursor()
    
    query = '''
        SELECT id, isim, telefon, email, meslek, kariyer_hedefi, haftalik_zaman, mesaj, tarih
        FROM leads
        ORDER BY tarih DESC
    '''
    
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    
    # sqlite3.Row nesnelerini standart Python sözlüklerine çeviriyoruz
    return [dict(row) for row in rows]
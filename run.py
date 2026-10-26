from app import create_app

# Uygulama fabrikası, ayarları yükleyip rotaları kaydeden Flask örneğini oluşturur.
app = create_app()

if __name__ == '__main__':
    # Geliştirme sunucusunu tüm ağ arayüzlerinden erişilebilir şekilde başlatır.
    app.run(
        host='0.0.0.0',
        port=5000,
        # Yapılandırmada DEBUG yoksa geliştirme kolaylığı için açık varsayılır.
        debug=app.config.get('DEBUG', True)
    )
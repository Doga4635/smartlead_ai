# hello.py — sadece ortam testi (proje dosyası DEĞİL)
from flask import Flask

# Ana uygulamadan bağımsız, Flask kurulumunu hızlıca sınamak için küçük bir örnek uygulama.
app = Flask(__name__)


@app.route("/")
def merhaba():
    # Ana sayfaya yapılan GET isteğinde sunucunun çalıştığını belirten metni döndürür.
    return "Ortam calisiyor!"  # <-- Başına 4 boşluk (girinti) eklendi


if __name__ == "__main__":
    # Test uygulamasını 5000 numaralı portta yerel varsayılanlarla çalıştırır.
    app.run(port=5000)
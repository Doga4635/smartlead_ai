import requests
from config import get_config

class AIServiceError(Exception):
    """AI Servisine özel hata sınıfı."""
    pass

class AIService:

    def __init__(self):
        self.config = get_config()
        # Aktif ve resmi Groq modeli
        self.model = "llama-3.1-8b-instant"  
        self.groq_url = "https://api.groq.com/openai/v1/chat/completions"

    def _get_system_prompt(self):
        """Sistem talimatını (BUSINESS_CONTEXT) config'den alır."""
        return self.config.BUSINESS_CONTEXT

    def yanit_uret(self, mesaj, gecmis=None):
        """
        Kullanıcı mesajını ve sohbet geçmişini alarak Groq API'sine gönderir, 
        üretilen yanıtı döndürür.
        """
        api_key = self.config.GROQ_API_KEY

        # DÜZELTİLDİ: Sadece anahtar yoksa, boşsa veya yer tutucu (default) ise demo moduna geçer
        if not api_key or api_key.strip() == "" or api_key == "gsk_your_actual_groq_api_key_here":
            return (
                "[DEMO MODU] Merhaba! Ben Callifex kariyer danışmanıyım. "
                "Şu an API anahtarı tanımlı olmadığı için demo modunda yanıt veriyorum. "
                "Yazılım, UI/UX tasarımı veya dijital pazarlama alanındaki kariyer hedefleriniz "
                "ve size özel eğitim yol haritamız hakkında bilgi almak için iletişim bilgilerinizi bırakabilirsiniz!"
            )

        if gecmis is None:
            gecmis = []

        # 1. İstek dizisini (messages) hazırlama
        messages = [
            {"role": "system", "content": self._get_system_prompt()}
        ]

        # 2. Geçmiş sohbet mesajlarını ekleme
        for node in gecmis:
            messages.append({
                "role": node.get("role", "user"),
                "content": node.get("content", "")
            })

        # 3. Son kullanıcı mesajını ekleme
        messages.append({"role": "user", "content": mesaj})

        headers = {
            "Authorization": f"Bearer {api_key.strip()}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7
        }

        # 4. API İsteği ve Hata Yönetimi
        try:
            response = requests.post(
                self.groq_url,
                json=payload,
                headers=headers,
                timeout=15
            )

            if response.status_code != 200:
                raise AIServiceError(
                    f"Groq API hatası döndürdü (Status {response.status_code}): {response.text}"
                )

            data = response.json()
            return data["choices"][0]["message"]["content"]

        except requests.exceptions.Timeout:
            raise AIServiceError("Yapay zekâ servisine yanıt süresi aşımına uğradı (Timeout).")
        except requests.exceptions.RequestException as e:
            raise AIServiceError(f"Yapay zekâ servisi ile bağlantı kurulamadı: {str(e)}")
        except (KeyError, IndexError) as e:
            raise AIServiceError(f"API yanıtı beklenmeyen bir formatta geldi: {str(e)}")

# Dosya sonunda tek bir servis örneği (Singleton pattern)
ai_service = AIService()
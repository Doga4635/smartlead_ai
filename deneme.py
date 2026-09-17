""" print("Merhaba Dünya")

print(2012)

print("15","05","2024",sep="/") """

""" print("Veriler",end=" ")
print("Yükleniyor") """

""" isim = "ahmet"
yas = 25
puan = 85.5

print("İsim: ",isim)
print("Yaş: ",yas)
print("Puan: ",puan) """

""" tam_isim = input("Tam isminizi giriniz: ")

print("Merhaba",tam_isim) """

""" gulumse = "ha"

print(gulumse*3) """

""" print(bool("ali")) """

""" fiyat = float(input("Fiyatı giriniz(sayı giriniz!!): "))
print("Fiyat: ",fiyat) """

""" sayi = 17
bolen = 3
print(sayi%bolen) """

""" temperature = float(input("Sıcaklığı giriniz: "))
if temperature > 30:
    print("Hava çok sıcak")
elif temperature > 20:  
    print("Hava sıcak")
elif temperature > 10:
    print("Hava ılık")
else:
    print("Hava soğuk") """

""" kelime = input("Kelimeyi giriniz: ")

for harf in kelime:
    print(harf)
    print("**********") """

""" right_password = "1234"
entered_password = ""

while entered_password != right_password:
    entered_password = input("Şifreyi giriniz: ")

    if entered_password != right_password:
        print("Hatalı şifre, tekrar deneyiniz.")

print("Şifre doğru, giriş yapıldı.") """

""" notlar = [70, 85, 90, 60, 75]

notlar.sort()

for not_ in notlar:
    print(not_) """

""" def square(a):
    return a ** 2

result = square(5)
print(result)

result2 = sum([1, 2, 3, 4, 5])
print(result2) """

""" puan = 85

puan2 = float(input("Lütfen puanınızı giriniz: "))

def not_hesapla(puan2):
    global puan
    if puan2 >= 90:
        return "A"
    elif puan2 >= 80:
        return "B"
    elif puan2  >= 70:
        return "C"
    elif puan2 >= 60:
        return "D"
    else:
        puan = 300
        return puan

print("Notunuz: ",not_hesapla(puan2))
print("Puanınız: ",puan) """

""" numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) """

""" try:
    sayi1 = int(input("Birinci sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    sonuc = sayi1 / sayi2
    print("Sonuç: ", sonuc)
except ZeroDivisionError:
    print("Hata: Sıfıra bölme hatası.")
except ValueError:
    print("Hata: Geçersiz giriş. Lütfen bir sayı giriniz.")

print("Program sonlandı.") """

""" students = [
    {"name": "Ali", "age": 20, "grade": 85},
    {"name": "Ayşe", "age": 22, "grade": 90},
    {"name": "Mehmet", "age": 19, "grade": 75},
] """

""" def add_student(name, age, grade):
    try:
        name = str(name)
        age = int(age)
        grade = int(grade)
        student = {"name": name, "age": age, "grade": grade}
        students.append(student)
    except ValueError:
        print("Hata: Yaş ve not sayısal değerler olmalıdır.")
        

def display_students():
    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grade:", student["grade"])
        print("-------------------")


while True:
    print("1. Öğrenci Ekle")
    print("2. Öğrencileri Göster")
    print("3. Çıkış")
    choice = input("Seçiminizi yapınız (1/2/3): ")

    if choice == "1":
        name = input("Öğrencinin adını giriniz: ")
        age = input("Öğrencinin yaşını giriniz: ")
        grade = input("Öğrencinin notunu giriniz: ")
        add_student(name, age, grade)
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyiniz.") """

""" dosya = open("ogrenciler.txt", "a")
dosya.write("Ali, 20, 85\n")
dosya.close() """

""" import math
import datetime

print(math.sqrt(16))

now = datetime.datetime.now()
print("Şu anki tarih ve saat:", now)
print("Yıl:", now.year)
print("Ay:", now.month)
print("Gün:", now.day) """


""" print(response.headers["Content-Type"])
if response.status_code == 200:
    print("GitHub API'den alınan veri:")
    print(response.text[0:50])  # İlk 100 karakteri yazdır
else:
    print("Hata: API isteği başarısız oldu. Durum kodu:", response.status_code) """

""" url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "foo",
    "body": "bar",
    "userId": 1
} """


""" try:
    response = requests.post(url, json=new_post)

    result = response.json()
    print("Yeni oluşturulan ID:")
    print(result["id"])

except requests.exceptions.RequestException as e:
    print("Hata: API isteği başarısız oldu.", e)
except requests.exceptions.Timeout:
    print("Hata: API isteği zaman aşımına uğradı.")
 """

from groq import Groq, APIError, RateLimitError
from flask import Flask
import requests
from dotenv import load_dotenv
import os

""" load_dotenv()

#api_key = os.getenv("GROQ_API_KEY")

print("GROQ API Anahtarı:", api_key)

print("ChatBot'a hoş geldiniz! Sorularınızı sorabilirsiniz.(Çıkmak için 'q' ye basınız.)")


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

questions = [
    {
        "role": "system",
        "content": "Sen bir yardımcı asistan olarak görev yapıyorsun."
    }
]

while True:
    user_input = input("Soru: ")
    if user_input.lower() == 'q':
        print("Programdan çıkılıyor...")
        break

    try:
        questions.append({
            "role": "user",
            "content": user_input
        })

        response = client.chat.completions.create(
            messages=[
                {
                "role": "user", 
                "content": questions
                },
            ],
            temperature=0.2,
            max_tokens=150,
            model="openai/gpt-oss-120b",
        )
    except RateLimitError as e:
        print("Hata: API isteği başarısız oldu. Rate limit aşıldı.", e)
    except APIError as e:
        print("Hata: API isteği başarısız oldu.", e)
    except Exception as e:
        print("Hata: API isteği başarısız oldu.", e)


    bot_response = response.choices[0].message.content
    print(bot_response)

    questions.append({
        "role": "assistant",
        "content": bot_response
    }) """

app = Flask(__name__)

@app.route('/selam/<name>')
def index(name):
    return f"Merhaba, {name} Flask uygulaması çalışıyor!"

@app.route('/square/<int:number>')
def square(number):
    return f"{number} sayısının karesi: {number ** 2}"

if __name__ == '__main__':
    app.run(debug=True)



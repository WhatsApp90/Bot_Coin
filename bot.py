import os
import time
import requests
import threading
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "✅ بوت الأذكار الإسلامي المتجدد يعمل بنجاح!"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

# 🌟 ضع توكن بوتك هنا:
TOKEN = "8707584108:AAGxDcoliR8gS8jwEo3ii_pktZ6U4FF1ZHg"

# 🌟 قائمة أرقام حسابك وحسابات إخوتك (تأكد أن الجميع ضغط Start في البوت أولاً)
CHAT_IDS = ["6856665810", "8955506857", "8688282197"] 

def get_random_zekr():
    """وظيفة ذكية تتصل بالإنترنت وتجلب ذكراً متجدداً في كل مرة"""
    try:
        # الاتصال بقاعدة بيانات أذكار إسلامية مفتوحة وموثوقة
        response = requests.get("https://githubusercontent.com")
        if response.status_code == 200:
            data = response.json()
            # جلب ذكر عشوائي من قائمة أذكار الصباح والمساء والتسابيح
            import random
            all_types = list(data.keys())
            random_type = random.choice(all_types)
            random_item = random.choice(data[random_type])
            return random_item.get('zekr') or random_item.get('content')
    except Exception as e:
        print(f"⚠️ فشل جلب ذكر متجدد، سيتم استخدام ذكر احتياطي: {e}", flush=True)
    
    # ذكر احتياطي في حال انقطع الإنترنت عن موقع الأذكار
    return "سبحان الله وبحمده، سبحان الله العظيم."

def send_islamic_message_to_all(text_content):
    if not TOKEN:
        print("❌ خطأ: التوكن غير موجود!", flush=True)
        return

    token_clean = TOKEN.strip()

    for chat_id in CHAT_IDS:
        chat_clean = str(chat_id).strip()
        url = f"https://telegram.org{token_clean}/sendMessage"
        payload = {
            "chat_id": chat_clean,
            "text": text_content,
            "parse_mode": "Markdown"
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"✅ [ناجح] تم إرسال الرسالة إلى الحساب: {chat_clean}", flush=True)
            else:
                print(f"❌ [خطأ] فشل الإرسال للحساب {chat_clean}. السبب: {response.text}", flush=True)
        except Exception as e:
            print(f"❌ [خطأ اتصال] مشكلة مع الحساب {chat_clean}: {e}", flush=True)

if __name__ == "__main__":
    print("🚀 جاري بدء تشغيل بوت الأذكار المتجدد...", flush=True)
    
    server_thread = threading.Thread(target=run_web_server)
    server_thread.daemon = True
    server_thread.start()
    
    # الرسالة الترحيبية الأولى فور تشغيل السيرفر
    first_message = (
        "✨ **مرحباً بكم في بوت الأذكار الإسلامي المتجدد!** ✨\n\n"
        "تم تشغيل البوت بنجاح ليشارككم الأذكار والآيات القرآنية المتغيرة تلقائياً وبدون تكرار.\n\n"
        "قال الله تعالى: 《أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ》\n\n"
        "🤍 سيصلكم الآن ذكر جديد ومختلف تماماً كل ساعة بإذن الله."
    )
    
    send_islamic_message_to_all(first_message)
    
    while True:
        # ينام الكود لمدة ساعة (3600 ثانية)
        time.sleep(3600) 
        
        # جلب ذكر جديد تماماً وغير مكرر من الإنترنت
        new_zekr = get_random_zekr()
        
        reminder = f"🕌 **تذكير متجدد بالذكر المبارك:**\n\n{new_zekr}"
        send_islamic_message_to_all(reminder)
                  

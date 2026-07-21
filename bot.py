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

# 🌟 هذا هو سطر التوكن الخاص بك الصحيح والدقيق تماماً الآن:
TOKEN = "8707584108:AAGxDcoliR8gS8jwEo3ii_pktZ6U4FF1ZHg"

# 🌟 قائمة أرقام الحسابات (حسابك وحسابات إخوتك)
CHAT_IDS = ["6856665810", "8955506857", "8688282197"] 

def get_random_zekr():
    try:
        response = requests.get("https://githubusercontent.com")
        if response.status_code == 200:
            data = response.json()
            import random
            all_types = list(data.keys())
            random_type = random.choice(all_types)
            random_item = random.choice(data[random_type])
            return random_item.get('zekr') or random_item.get('content')
    except Exception as e:
        print(f"⚠️ فشل جلب ذكر متجدد: {e}", flush=True)
    return "سبحان الله وبحمده، سبحان الله العظيم."

def send_islamic_message_to_all(text_content):
    token_clean = TOKEN.strip()

    for chat_id in CHAT_IDS:
        chat_clean = str(chat_id).strip()
        # الرابط الصحيح والمباشر مع التوكن النظيف
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
                print(f"❌ [خطأ تليجرام] الحساب {chat_clean} رفض الإرسال. التفاصيل: {response.text}", flush=True)
        except Exception as e:
            print(f"❌ [خطأ اتصال] مشكلة مع الحساب {chat_clean}: {e}", flush=True)

if __name__ == "__main__":
    print("🚀 جاري بدء تشغيل بوت الأذكار بالتودكن الصحيح...", flush=True)
    
    server_thread = threading.Thread(target=run_web_server)
    server_thread.daemon = True
    server_thread.start()
    
    first_message = (
        "✨ **مرحباً بكم في بوت الأذكار الإسلامي المتجدد!** ✨\n\n"
        "تم تشغيل البوت بنجاح ويشارككم الأذكار والآيات القرآنية المتغيرة تلقائياً.\n\n"
        "قال الله تعالى: 《أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ》\n\n"
        "🤍 سيصلكم الآن ذكر جديد ومختلف تماماً كل ساعة بإذن الله."
    )
    
    send_islamic_message_to_all(first_message)
    
    while True:
        time.sleep(3600) 
        new_zekr = get_random_zekr()
        reminder = f"🕌 **تذكير متجدد بالذكر المبارك:**\n\n{new_zekr}"
        send_islamic_message_to_all(reminder)
        

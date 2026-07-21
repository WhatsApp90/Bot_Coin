import os
import time
import requests
import threading
from flask import Flask

# 1. إنشاء خادم ويب مصغر لإرضاء Render و UptimeRobot
app = Flask('')

@app.route('/')
def home():
    return "✅ بوت الأذكار الإسلامي يعمل بنجاح!"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

# 2. جلب المتغيرات البيئية
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("YOUR_CHAT_ID")

def send_islamic_message(text_content):
    if not TOKEN or not CHAT_ID:
        print("❌ خطأ: المتغيرات غير موجودة في إعدادات Render!", flush=True)
        return

    # تنظيف المتغيرات من أي مسافات زائدة
    token_clean = TOKEN.strip()
    chat_clean = CHAT_ID.strip()

    # الرابط الصحيح والمباشر لتليجرام
    url = f"https://telegram.org{token_clean}/sendMessage"
    payload = {
        "chat_id": chat_clean,
        "text": text_content,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ [ناجح] تم إرسال الرسالة الإسلامية إلى تليجرام!", flush=True)
        else:
            print(f"❌ [خطأ] تليجرام رفض الإرسال. السبب: {response.text}", flush=True)
    except Exception as e:
        print(f"❌ [خطأ اتصال] فشل الاتصال بتليجرام: {e}", flush=True)

if __name__ == "__main__":
    print("🚀 جاري بدء تشغيل بوت الأذكار الإسلامي...", flush=True)
    
    # تشغيل خادم الويب في الخلفية لضمان استقرار المنصة
    server_thread = threading.Thread(target=run_web_server)
    server_thread.daemon = True
    server_thread.start()
    
    # 🌟 الرسالة الأولى والأساسية التي ستصلك فوراً عند اشتغال السيرفر
    first_message = (
        "✨ **مرحباً بك في بوت الأذكار الإسلامي التلقائي!** ✨\n\n"
        "تم تشغيل البوت بنجاح على سيرفر Render العالمي.\n\n"
        "قال الله تعالى: 《الَّذِينَ آمَنُوا وَتَطْمَئِنُّ قُلُوبُهُم بِذِكْرِ اللَّهِ ۗ أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ》\n\n"
        "🤍 البوت سيبدأ الآن بإرسال تذكير وأذكار لك بشكل دوري تلقائياً."
    )
    
    # إرسال الرسالة الفورية
    send_islamic_message(first_message)
    
    # قائمة بأذكار متنوعة يرسلها البوت كل ساعة لإبقاء السيرفر حياً
    azkar_list = [
        "🌸 سبحان الله وبحمده، سبحان الله العظيم.",
        "✨ لا إله إلا أنت سبحانك إني كنت من الظالمين.",
        "🤍 أستغفر الله العظيم وأتوب إليه.",
        "اللهم صلِّ وسلم وبارك على نبينا محمد وعلى آله وصحبه أجمعين."
    ]
    
    index = 0
    while True:
        # ينام الكود لمدة ساعة (3600 ثانية) ثم يرسل الذكر التالي
        time.sleep(3600)
        reminder = f"🕌 **تذكير بالذكر الصباحي/المسائي:**\n\n{azkar_list[index]}"
        send_islamic_message(reminder)
        
        # الانتقال للذكر التالي في القائمة
        index = (index + 1) % len(azkar_list)
        

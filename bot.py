import os
import time
import requests
import threading
from flask import Flask

# 1. إنشاء خادم ويب مصغر لإرضاء UptimeRobot
app = Flask('')

@app.route('/')
def home():
    return "✅ البوت يعمل بنجاح في الخلفية!"

def run_web_server():
    # تشغيل السيرفر على المنفذ 8080 المعتمد في منصات الاستضافة
    app.run(host='0.0.0.0', port=8080)

# 2. وظيفة البوت الأساسية لإرسال الرسائل
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("YOUR_CHAT_ID")

def send_crypto_opportunities():
    message = (
        "🌟 **مرحباً بك! إليك المواقع الآمنة والموثوقة لجمع العملات مجاناً اليوم:**\n\n"
        "1️⃣ **CoinPayU**\n"
        "🔗 الرابط: [اضغط هنا](https://coinpayu.com)\n"
        "📝 طريقة الربح: مشاهدة إعلانات بسيطة وجمع ساتوشي (بيتكوين مجاني).\n\n"
        "2️⃣ **FreeBitco.in**\n"
        "🔗 الرابط: [اضغط هنا](https://freebitco.in)\n"
        "📝 طريقة الربح: تدوير العجلة مجاناً كل ساعة للحصول على بيتكوين.\n\n"
        "3️⃣ **FaucetPay**\n"
        "🔗 الرابط: [اضغط هنا](https://faucetpay.io)\n"
        "📝 نصيحة: افتح حساباً هنا أولاً، لأنه المحفظة المصغرة التي تستقبل عليها الأرباح من كل المواقع الأخرى.\n\n"
        "⚠️ **تنبيه عمو المهم لحمايتك:**\n"
        "• إذا طلب منك أي موقع دفع سنت واحد لتسحب، أغلقه فوراً فهو نصاب.\n"
        "• لا تعطي كلمات محفظتك السرية لأي شخص أو موقع إطلاقاً."
    )
    
    url = f"https://telegram.org{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ تم إرسال قائمة الفرص بنجاح إلى حسابك في تليجرام!")
        else:
            print(f"❌ فشل الإرسال. خطأ: {response.text}")
    except Exception as e:
        print(f"❌ حدث خطأ في الاتصال: {e}")

if __name__ == "__main__":
    if not TOKEN or not CHAT_ID:
        print("❌ خطأ: يرجى إضافة المتغيرات البيئية في إعدادات المنصة!")
    else:
        print("🚀 البوت بدأ العمل...")
        
        # تشغيل خادم الويب في مسار جانبي (Thread) لكي لا يعطل البوت
        server_thread = threading.Thread(target=run_web_server)
        server_thread.daemon = True
        server_thread.start()
        
        # إرسال الرسالة لتليجرام فوراً عند التشغيل
        send_crypto_opportunities()
        
        # حلقة التكرار لإبقاء السيرفر حياً
        while True:
            time.sleep(3600)
        

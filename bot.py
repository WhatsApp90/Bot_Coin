import os
import time
import requests
import threading
from flask import Flask

# 1. تشغيل خادم الويب لإبقاء البوت حياً على Render و UptimeRobot
app = Flask('')

@app.route('/')
def home():
    return "✅ البوت يعمل بنجاح في الخلفية!"

def run_web_server():
    # تشغيل السيرفر على المنفذ 8080 المعتمد في ريندر
    app.run(host='0.0.0.0', port=8080)

# 2. جلب وتجهيز متغيرات تليجرام
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("YOUR_CHAT_ID")

def send_crypto_opportunities():
    # إزالة أي مسافات زائدة قد تحدث بالخطأ عند النسخ واللصق
    token_clean = TOKEN.strip() if TOKEN else None
    chat_clean = CHAT_ID.strip() if CHAT_ID else None

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
    
    url = f"https://telegram.org{token_clean}/sendMessage"
    payload = {
        "chat_id": chat_clean,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ [ناجح] تم إرسال قائمة الفرص بنجاح إلى تليجرام!")
        else:
            # هنا السيرفر سيكشف لنا بدقة سبب المشكلة إذا رفض تليجرام إرسال الرسالة
            print(f"❌ [خطأ تليجرام] فشل الإرسال! الرمز: {response.status_code} - التفاصيل: {response.text}")
    except Exception as e:
        print(f"❌ [خطأ اتصال] حدثت مشكلة أثناء الاتصال بتليجرام: {e}")

if __name__ == "__main__":
    if not TOKEN or not CHAT_ID:
        print("❌ خطأ: يرجى إضافة المتغيرات البيئية في إعدادات المنصة!")
    else:
        print("🚀 البوت بدأ العمل وفحص المتغيرات...")
        
        # تشغيل خادم الويب في الخلفية
        server_thread = threading.Thread(target=run_web_server)
        server_thread.daemon = True
        server_thread.start()
        
        # حلقة تكرار ترسل الرسالة فوراً ثم تعيد المحاولة كل 60 ثانية لتسهيل الفحص
        while True:
            send_crypto_opportunities()
            print("💤 البوت في وضع الانتظار لمدة دقيقة قبل المحاولة القادمة...")
            time.sleep(60)
    

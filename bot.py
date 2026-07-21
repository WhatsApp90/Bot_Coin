import os
import time
import requests
import threading
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "✅ البوت يعمل بنجاح في الخلفية!"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("YOUR_CHAT_ID")

def send_crypto_opportunities():
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
        "• إذا طلب منك أي موقع دفع سنت واحد لتسحب, أغلقه فوراً فهو نصاب.\n"
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
            print("✅ [ناجح] تم إرسال قائمة الفرص بنجاح إلى تليجرام!", flush=True)
        else:
            print(f"❌ [خطأ تليجرام] فشل الإرسال! الرمز: {response.status_code} - التفاصيل: {response.text}", flush=True)
    except Exception as e:
        print(f"❌ [خطأ اتصال] مشكلة في الاتصال بتليجرام: {e}", flush=True)

if __name__ == "__main__":
    if not TOKEN or not CHAT_ID:
        print("❌ خطأ: يرجى إضافة المتغيرات البيئية في إعدادات المنصة!", flush=True)
    else:
        print("🚀 البوت بدأ العمل وفحص المتغيرات...", flush=True)
        
        server_thread = threading.Thread(target=run_web_server)
        server_thread.daemon = True
        server_thread.start()
        
        while True:
            send_crypto_opportunities()
            print("💤 البوت في وضع الانتظار لمدة دقيقة...", flush=True)
            time.sleep(60)
            

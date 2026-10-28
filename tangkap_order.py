import time, json, os, smtplib
from datetime import datetime
from email.mime.text import MIMEText
import subprocess

# CONFIG - PUNYA KAMU
EMAIL = "rafipecintadunia@gmail.com"
APP_PASS = "eynhsjwjtvdbfobs"
REPO_PATH = os.path.expanduser("~/gmail-termux")
ORDERS_FILE = os.path.join(REPO_PATH, "indrive_orders.json")
LOG_FILE = os.path.join(REPO_PATH, "indrive_orders.log")

def kirim_email(judul, isi):
    try:
        msg = MIMEText(isi)
        msg['Subject'] = judul
        msg['From'] = EMAIL
        msg['To'] = EMAIL
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, APP_PASS)
        server.send_message(msg)
        server.quit()
        print(f"✅ Email terkirim: {judul}")
        return True
    except Exception as e:
        print(f"❌ Gagal email: {e}")
        return False

def push_github(pesan):
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "add", "."], check=False)
        subprocess.run(["git", "commit", "-m", pesan], check=False)
        subprocess.run(["git", "push"], check=False)
        print(f"✅ Push GitHub: {pesan}")
    except Exception as e:
        print(f"❌ Gagal push: {e}")

def baca_orders():
    if not os.path.exists(ORDERS_FILE):
        return []
    try:
        with open(ORDERS_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

print("=== APLIKASI TANGKAP ORDERAN PAMEKASAN ===")
print("Logger: Termux + GitHub + Gmail - Aktif!")
print(f"Memantau: {ORDERS_FILE}")
print("Tekan CTRL+C untuk berhenti\n")

orders_lama = baca_orders()
print(f"Order awal: {len(orders_lama)} order")

# Kirim email startup
kirim_email(
    f"inDrive LOGGER AKTIF {datetime.now().strftime('%H:%M WIB')}",
    f"Halo Rafi,\n\nLogger Pamekasan aktif di Surabaya!\nMemantau {len(orders_lama)} order lama.\n\nSistem: Termux + GitHub + Gmail\nWaktu: {datetime.now()}\n\n- Logger Pamekasan"
)
push_github(f"Logger aktif {datetime.now().strftime('%Y-%m-%d %H:%M')}")

while True:
    try:
        time.sleep(10)  # Cek tiap 10 detik
        orders_baru = baca_orders()
        
        if len(orders_baru) > len(orders_lama):
            selisih = len(orders_baru) - len(orders_lama)
            order_terbaru = orders_baru[-1]
            
            print(f"\n🔥 ORDER BARU! +{selisih} - Total {len(orders_baru)}")
            print(f"Data: {order_terbaru}")
            
            # Bikin pesan
            judul = f"inDrive ORDER BARU {datetime.now().strftime('%H:%M WIB')} - Pamekasan"
            isi = f"""Ada order baru masuk!

Waktu: {datetime.now().strftime('%d %b %Y %H:%M:%S')}
Total Order: {len(orders_baru)}
Order Baru: {selisih}

Data Terbaru:
{json.dumps(order_terbaru, indent=2, ensure_ascii=False)}

File Log: {LOG_FILE}
Lokasi: Surabaya -> Pamekasan Logger

- Auto Tangkap Order System
Termux + GitHub + Gmail
"""
            # Kirim email + push github
            kirim_email(judul, isi)
            push_github(f"Order baru {datetime.now().strftime('%H:%M')} - Total {len(orders_baru)}")
            
            orders_lama = orders_baru
        else:
            print(f".", end="", flush=True)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Logger dihentikan Rafi!")
        break
    except Exception as e:
        print(f"\nError: {e}")
        time.sleep(5)

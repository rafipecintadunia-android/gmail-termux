import smtplib
from email.mime.text import MIMEText

# AKUN KAMU YANG UDAH JADI TADI
EMAIL = "rafipecintadunia@gmail.com"
APP_PASS = "eynhsjwjtvdbfobs"  # secret baru yang 1% tadi

msg = MIMEText("Halo, ini dikirim lewat project yang terhubung GitHub + Termux + Gmail. Logger Pamekasan aktif! - Dikirim dari Termux Surabaya")
msg['Subject'] = "Tes dari GitHub + Termux Pamekasan"
msg['From'] = EMAIL
msg['To'] = EMAIL

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL, APP_PASS)
    server.send_message(msg)
    server.quit()
    print("✅ BERHASIL! Email terkirim dari Termux!")
except Exception as e:
    print(f"❌ Gagal: {e}")

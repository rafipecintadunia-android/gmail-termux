import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_KAMU = "rafipecintadunia@gmail.com"
APP_PASSWORD = "ghkeodbdfivrnyrf"
TUJUAN = "rafipecintadunia@gmail.com"

msg = MIMEMultipart()
msg['From'] = EMAIL_KAMU
msg['To'] = TUJUAN
msg['Subject'] = "Tes dari Termux Pamekasan"

body = "Halo, ini tes kirim email dari HP via Termux! Berhasil."
msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_KAMU, APP_PASSWORD)
    server.send_message(msg)
    server.quit()
    print("[OK] Email terkirim!")
except Exception as e:
    print(f"[GAGAL] {e}")

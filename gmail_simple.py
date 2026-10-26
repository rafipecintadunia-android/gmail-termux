import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Ambil dari Environment, bukan ditulis langsung
email = os.getenv("GMAIL_USER")
app = os.getenv("GMAIL_APP")
tujuan = os.getenv("GMAIL_TO") or input("Kirim ke: ").strip()

if not email or not app:
    print("Set dulu: export GMAIL_USER dan GMAIL_APP di Termux / GitHub Secrets")
    exit()

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = tujuan
msg['Subject'] = "Tes dari GitHub + Termux Pamekasan"
msg.attach(MIMEText("Halo, ini dikirim lewat project yang terhubung ke GitHub!", 'plain'))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, app)
server.send_message(msg)
server.quit()
print(f"[OK] Email terkirim dari {email} ke {tujuan}!")

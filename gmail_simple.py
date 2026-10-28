import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "rafipecintadunia@gmail.com"
app = "eynhsjwjtvdbfobs"
tujuan = "rafipecintadunia@gmail.com"

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = tujuan
msg['Subject'] = "Tes dari GitHub + Termux Pamekasan"
msg.attach(MIMEText("Halo, ini dikirim lewat project yang terhubung GitHub + Termux + Gmail. Logger Pamekasan aktif!"))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, app)
server.send_message(msg)
server.quit()
print(f"[OK] Email terkirim dari {email} ke {tujuan}!")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import json, os, smtplib
from email.mime.text import MIMEText
from datetime import datetime

EMAIL = "rafipecintadunia@gmail.com"
APP_PASS = "eynhsjwjtvdbfobs"

class LoggerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.status = Label(text="inDrive Logger Pamekasan\nSurabaya - Aktif!", font_size=20)
        self.info = Label(text="Order: 3 | Email: 01:44 WIB sukses\nGitHub: e13643e push ok", font_size=14)
        
        btn_test = Button(text="TES KIRIM EMAIL", background_color=(0,1,0,1), height=80, size_hint_y=None)
        btn_test.bind(on_press=self.kirim_email)
        
        btn_order = Button(text="CEK ORDER", background_color=(0,0,1,1), height=80, size_hint_y=None)
        btn_order.bind(on_press=self.cek_order)
        
        self.layout.add_widget(self.status)
        self.layout.add_widget(self.info)
        self.layout.add_widget(btn_test)
        self.layout.add_widget(btn_order)
        return self.layout

    def kirim_email(self, instance):
        try:
            msg = MIMEText(f"Test dari APK Pamekasan! Waktu {datetime.now()}")
            msg['Subject'] = f"APK LOGGER AKTIF {datetime.now().strftime('%H:%M WIB')}"
            msg['From'] = EMAIL
            msg['To'] = EMAIL
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL, APP_PASS)
            server.send_message(msg)
            server.quit()
            self.info.text = f"✅ Email terkirim {datetime.now().strftime('%H:%M:%S')}"
        except Exception as e:
            self.info.text = f"❌ Gagal: {e}"

    def cek_order(self, instance):
        try:
            if os.path.exists("indrive_orders.json"):
                with open("indrive_orders.json") as f:
                    data = json.load(f)
                self.info.text = f"Total Order: {len(data)} order\nTerakhir: {datetime.now()}"
            else:
                self.info.text = "Belum ada indrive_orders.json"
        except Exception as e:
            self.info.text = f"Error: {e}"

LoggerApp().run()

from kivy.app import App
from kivy.uix.label import Label
class LoggerApp(App):
    def build(self):
        return Label(text='Logger Pamekasan - Rafi\nAPK Berhasil!')
LoggerApp().run()

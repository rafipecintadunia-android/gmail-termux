from kivy.app import App
from kivy.uix.label import Label

class LoggerApp(App):
    def build(self):
        return Label(text='Logger Pamekasan - 3 Order - 01:44 - Rafi')

LoggerApp().run()

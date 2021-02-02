from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

class Container(MDBoxLayout):
    pass

class mynurse(MDApp):
    def build(self):
        return Container()

Window.size = (300, 500)
mynurse().run()

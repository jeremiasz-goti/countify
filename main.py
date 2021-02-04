from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class HomeScreen(Screen):
    pass

class PillScreen(Screen):
    pass

class DoctorScreen(Screen):
    pass

class BookScreen(Screen):
    pass

class ViewManager(ScreenManager):
    pass

class mynurse(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        kv = Builder.load_file('main.kv')
        return kv

Window.size = (300, 500)
mynurse().run()

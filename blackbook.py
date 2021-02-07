from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.navigationdrawer import NavigationLayout, MDNavigationDrawer

class Container(BoxLayout):
    pass


class mynurse(MDApp):
    def build(self):
        theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Teal"
        kv = Builder.load_file('test.kv')
        return kv


mynurse().run()

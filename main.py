from kivy.lang import builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRectangleFlatButton, MDTextButton



class Container(MDBoxLayout):
    pass

class Countify(MDApp):
    def build(self):
        return Container()

Window.size = (300, 500)
Countify().run()

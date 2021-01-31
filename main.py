from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class Container(FloatLayout):
    pass

class Countify(MDApp):
    def build(self):
        # screen = Screen()
        # screen.add_widget(
        #     MDRectangleFlatButton(
        #         text="Ustal budżet",
        #         pos_hint={"center_x": 0.5, "center_y": 0.55},
        #     )
        # )
        # screen.add_widget(    
        #     MDRectangleFlatButton(
        #         text="Historia zakupów",
        #         pos_hint={"center_x": 0.5, "center_y": 0.45},
        #     )
        # )

        return Container()

Countify().run()
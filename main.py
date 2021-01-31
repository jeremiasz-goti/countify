from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class Countify(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Ustal budżet",
                pos_hint={"center_x": 0.5, "center_y": 0.55},
            )
        )
        screen.add_widget(    
            MDRectangleFlatButton(
                text="Historia zakupów",
                pos_hint={"center_x": 0.5, "center_y": 0.45},
            )
        )

        return screen


Countify().run()
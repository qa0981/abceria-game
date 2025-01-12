from kivy.uix.screenmanager import Screen
from magic_image import MagicImage
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import MagicBehavior
from kivy.animation import Animation
from kivy.lang import Builder
from kivymd.app import MDApp

class ClickableImage(ButtonBehavior, Image):
    pass

class NameInputScreen(Screen):
    def on_enter(self):
        self.animate_floating(self.ids.animasi1, base_y=700)
        self.animate_floating(self.ids.animasi2, base_y=60)

    def animate_floating(self, widget, base_y):
        if widget:

            widget.y = base_y
            widget.x = widget.x

            floating = (
                Animation(y=base_y + 20, duration=0.6, t="in_out_quad") +
                Animation(y=base_y - 20, duration=0.6, t="in_out_quad")
            )
            floating.repeat = True
            floating.start(widget)
        else:
            print(f"Widget {widget} not found for animation!")

    def submit_username(self, username):
        if username.strip():
            def navigate_to_game():
                self.manager.get_screen("game").username = username
                self.manager.current = "game"

            self.ids.start_button.wobble_and_navigate(navigate_to_game)
        else:
            print("Username cannot be empty!")

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("paint.kv")
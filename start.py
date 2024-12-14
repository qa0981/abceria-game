from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation

class ClickableImage(ButtonBehavior, Image):
    pass


class StartScreen(Screen):
    def on_enter(self):
        self.animate_floating(self.ids.animasi1, base_y=700)
        self.animate_floating(self.ids.animasi2, base_y=60)
        self.animate_floating(self.ids.animasi3, base_y=550)

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

    def on_button_click(self, button_id):
        if button_id == "play":
            self.start_game()
        elif button_id == "quit":
            self.quit_app()

    def start_game(self):
        self.manager.current = "game"
        print("Starting game...")

    def quit_app(self):
        App.get_running_app().stop()
        print("Exiting app...")

    def open_options_popup(self):
        popup = OptionsPopup()
        popup.open()

class OptionsPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save_settings(self):
        print("Settings saved")

    def load_settings(self):
        return 0.5, 0.5

    def reset_settings(self):
        return 0.5, 0.5
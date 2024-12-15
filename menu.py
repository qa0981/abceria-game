from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.image import Image
from magic_image import MagicImage
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from functools import partial


def rgb(r, g, b, a=1):
    return r / 255, g / 255, b / 255, a

class ClickableImage(ButtonBehavior, Image):
    pass

class GameScreen(Screen):
    coin_count = StringProperty("100")
    username = StringProperty("Username")

    def go_to_start_menu(self):
        print("Returning to start menu")
        self.manager.current = "start"

    def start_game1(self):
        print("Game 1 clicked!")
        self.manager.current = "level_selection"

    def start_game2(self):
        print("Game 2 clicked!")
        self.manager.current = "game2"

    def start_game3(self):
        print("Game 3 clicked!")
        self.manager.current = "game3"

    def start_game4(self):
        print("Game 4 clicked!")
        self.manager.current = "game4"

    def start_game5(self):
        print("Game 5 clicked!")
        self.manager.current = "game5"

    def show_popup(self):
        popup = LevelSelectionPopup()
        popup.open()

    def update_coin_count(self, new_coin_count):
        self.coin_count = str(new_coin_count)

    def update_username(self, new_username):
        self.username = new_username

class LevelSelectionPopup(Popup):
    coin_count = StringProperty("100")
    username = StringProperty("Player")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.6, 0.7)
        self.auto_dismiss = False
        self.background = "image/bgp.png"

        content_layout = FloatLayout()

        title_image = Image(
            source="image/title/1.png",
            size_hint=(0.5, 0.2),
            pos_hint={"center_x": 0.5, "top": 0.95}
        )
        content_layout.add_widget(title_image)

        grid = GridLayout(cols=3, spacing=30, size_hint=(0.8, 0.5), pos_hint={"center_x": 0.5, "top": 0.7})
        for i in range(1, 4):
            button = Button(
                background_normal=f"buttons/button_level/{i}.png",
                size_hint=(None, None),
                size=(250, 250),
                on_release=partial(self.select_level, i)  # Corrected button handler
            )
            grid.add_widget(button)

        content_layout.add_widget(grid)

        close_button = ClickableImage(
            source="image/playy.png",
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={"center_x": 0.5, "y": 0.1}
        )
        close_button.bind(on_release=self.dismiss)
        content_layout.add_widget(close_button)

        self.content = content_layout

    def select_level(self, level):
        print(f"Level {level} selected!")
        self.dismiss()
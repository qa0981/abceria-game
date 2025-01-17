from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.image import Image
from magic_image import MagicImage
from kivy.properties import StringProperty, NumericProperty
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


def rgb(r, g, b, a=1):
    return r / 255, g / 255, b / 255, a

class ClickableImage(ButtonBehavior, Image):
    pass

class GameScreen(Screen):
    score = NumericProperty(0)
    username = StringProperty("Username")

    def play_sound(self, sound_path):
        sound = SoundLoader.load(sound_path)
        if sound:
            sound.play()

    def go_to_start_menu(self):
        print("Returning to start menu")
        self.manager.current = "start"
        self.play_sound("music/press-btn-next-back.mp3")

    def start_game1(self):
        print("Navigating to Game 1!")
        self.manager.current = "game1"
        self.play_sound("music/pop-button.mp3")

    def start_game2(self):
        print("Game 2 clicked!")
        self.manager.current = "tracing_1"
        self.play_sound("music/pop-button.mp3")

    def start_game3(self):
        print("Game 3 clicked!")
        self.manager.current = "kuis"
        self.play_sound("music/pop-button.mp3")

    def update_coin_count(self, new_coin_count):
        self.coin_count = str(new_coin_count)

    def update_username(self, new_username):
        self.username = new_username

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("paint.kv")
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.properties import StringProperty

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

    def update_coin_count(self, new_coin_count):
        self.coin_count = str(new_coin_count)

    def update_username(self, new_username):
        self.username = new_username

class LevelSelectionScreen(Screen):
    coin_count = StringProperty("100")
    username = StringProperty("Username")

    def select_level(self, level):
        print(f"Level {level} selected!")
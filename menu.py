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

class LevelSelectionScreen(Screen):
    def select_level(self, level):
        print(f"Level {level} selected!")
        # Navigate or load the selected level
        # For example:
        if level == 1:
            self.manager.current = "level1"
        elif level == 2:
            self.manager.current = "level2"
        elif level == 3:
            self.manager.current = "level3"

    def go_back(self):
        print("Returning to game screen")
        self.manager.current = "game"
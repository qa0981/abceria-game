from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
import string


class Game1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=20, padding=20)

        grid_container = BoxLayout(size_hint=(0.8, 0.7), pos_hint={"center_x": 0.5, "center_y": 0.5})
        grid = GridLayout(cols=7, spacing=10, padding=10, size_hint=(1, 1))
        for index, letter in enumerate(string.ascii_uppercase, start=1):
            image_path = f"image/huruf/btn/{letter}.png"
            sound_path = f"image/voice_ alfabet/{index}.mp3"
            image_button = ImageButton(
                source=image_path, sound_path=sound_path, size_hint=(0.13, 0.15)
            )
            grid.add_widget(image_button)
        grid_container.add_widget(grid)
        layout.add_widget(grid_container)

        self.add_widget(layout)

    def go_back(self, instance=None):
        self.manager.current = "game"


class ImageButton(Button):
    source = StringProperty("")
    sound_path = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = self.source
        self.background_down = self.source
        self.background_color = (1, 1, 1, 1)
        self.text = ""

    def on_press(self):
        if self.sound_path:
            print(f"Attempting to load sound: {self.sound_path}")
            sound = SoundLoader.load(self.sound_path)
            if sound:
                sound.play()
                print(f"Playing sound: {self.sound_path}")
            else:
                print(f"Sound file could not be loaded: {self.sound_path}")
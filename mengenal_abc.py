from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
import string


class Game1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical")

        title_bar = BoxLayout(size_hint=(1, 0.1), padding=10)
        title_bar.add_widget(Label(text="Game 1", font_size=24))
        back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.go_back)
        title_bar.add_widget(back_button)
        layout.add_widget(title_bar)

        grid = GridLayout(cols=8, spacing=10, padding=20)
        for index, letter in enumerate(string.ascii_uppercase, start=1):
            image_path = f"image/huruf/button/{letter}.png"
            sound_path = f"image/voice_ alfabet/{index}.mp3"
            image_button = ImageButton(
                source=image_path, sound_path=sound_path, size_hint=(220, 190)
            )
            grid.add_widget(image_button)
        layout.add_widget(grid)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = "game_screen"


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
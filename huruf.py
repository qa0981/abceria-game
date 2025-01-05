from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

class LevelOneScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_alphabet_buttons()

    def create_alphabet_buttons(self):
        # Create a GridLayout to hold the buttons
        grid = GridLayout(cols=6, spacing=10, padding=20, size_hint=(1, 0.9))
        self.add_widget(grid)

        # Add 26 alphabet buttons
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            button = Button(
                background_normal=f"images/alphabets/{char.lower()}.png",
                size_hint=(None, None),
                size=(100, 100),
                on_release=lambda btn, c=char: self.play_sound(c)
            )
            grid.add_widget(button)

    def play_sound(self, char):
        sound = SoundLoader.load(f"sounds/alphabets/{char.lower()}.mp3")
        if sound:
            sound.play()
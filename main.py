from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from input import NameInputScreen
from start import StartScreen
from menu import GameScreen
from draw import PaintScreen
from mengenal_abc import Game1Screen
from tracing import TracingScreen
from kivy.core.audio import SoundLoader


class PaintApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.music_player = None

    def build(self):
        self.rgb = lambda r, g, b, a=1: (r / 255, g / 255, b / 255, a)

        self.music_player = SoundLoader.load("music/backsound1.mp3")
        if self.music_player:
            self.music_player.loop = True
            self.music_player.volume = 0.5
            self.music_player.play()
        
        sm = ScreenManager()
        # sm.add_widget(NameInputScreen(name="name_input"))
        # sm.add_widget(StartScreen(name="start"))
        sm.add_widget(GameScreen(name="game"))
        sm.add_widget(Game1Screen(name="game1"))
        sm.add_widget(TracingScreen(name="game2"))
        # sm.add_widget(PaintScreen(name="paint"))
        return sm
    
    def on_stop(self):
        if self.music_player:
            self.music_player.stop()

if __name__ == "__main__":
    PaintApp().run()
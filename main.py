from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from input import NameInputScreen
from start import StartScreen
from menu import GameScreen
from draw import PaintScreen
from mengenal_abc import Game1Screen
from tracing import TracingScreen
from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import NumericProperty

Config.set("graphics", "resizable", True)


class PaintApp(MDApp):
    background_music = None
    music_volume = NumericProperty(0.5)


    def load_background_music(self):
        self.background_music = SoundLoader.load("music/backsound1.mp3")
        if self.background_music:
            self.background_music.volume = self.music_volume
            self.background_music.loop = True
            self.background_music.play()

    def build(self):
        Window.size = (640, 360)
        self.rgb = lambda r, g, b, a=1: (r / 255, g / 255, b / 255, a)

        self.load_background_music()
        
        sm = ScreenManager()
        sm.add_widget(NameInputScreen(name="name_input"))
        sm.add_widget(StartScreen(name="start"))
        sm.add_widget(GameScreen(name="game"))
        sm.add_widget(Game1Screen(name="game1"))
        for number in range(1, 27):
            sm.add_widget(TracingScreen(name=f"tracing_{number}", letter_number=str(number)))
        sm.current = "start"
        # sm.add_widget(PaintScreen(name="paint"))
        return sm
    
    def set_music_volume(self, volume):
        self.music_volume = volume
        if self.music:
            self.music.volume = volume
            print(f"Music volume updated to: {volume}")
    
    def on_stop(self):
        if self.background_music:
            self.background_music.stop()

if __name__ == "__main__":
    PaintApp().run()
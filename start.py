from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty

class ClickableImage(ButtonBehavior, Image):
    pass


class StartScreen(Screen):
    def on_enter(self):
        self.start_animations()

    def start_animations(self):
        anim1 = self.ids.anim1
        if anim1:
            floating = (
                Animation(y=anim1.y + 20, duration=1, t='in_out_quad') +
                Animation(y=anim1.y - 20, duration=1, t='in_out_quad')
            )
            floating.repeat = True
            floating.start(anim1)

        anim2 = self.ids.anim2
        if anim2:
            bouncing = (
                Animation(y=anim2.y + 30, duration=0.8, t='out_bounce') +
                Animation(y=anim2.y - 40, duration=0.8, t='out_bounce')
            )
            bouncing.repeat = True
            bouncing.start(anim2)

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
        popup = OptionsPopup(app=MDApp.get_running_app())
        popup.open()

class OptionsPopup(Popup):
    sound_volume = NumericProperty(0.5)
    music_volume = NumericProperty(0.5)

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.sound_volume = app.sound_volume 
        self.music_volume = app.music_volume 

    def on_sound_volume_change(self, instance, value):
        self.app.sound_volume = value
        if self.app.background_music:
            self.app.background_music.volume = value

    def on_music_volume_change(self, instance, value):
        self.app.music_volume = value
        if self.app.background_music:
            self.app.background_music.volume = value

    def save_settings(self):
        print(f"Sound Volume: {self.sound_volume}, Music Volume: {self.music_volume}")
    
    def reset_to_defaults(self):
        self.sound_volume = 0.5
        self.music_volume = 0.5
        self.app.sound_volume = 0.5
        self.app.music_volume = 0.5
        if self.app.background_music:
            self.app.background_music.volume = 0.5
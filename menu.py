from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.image import Image
from magic_image import MagicImage
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.switch import Switch
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp


def rgb(r, g, b, a=1):
    return r / 255, g / 255, b / 255, a

class ClickableImage(ButtonBehavior, Image):
    pass

class GameScreen(Screen):
    score = NumericProperty(0)
    username = StringProperty("Username")
    background_sound_active = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = None

        layout = FloatLayout()

        settings_button = Button(
            size_hint=(None, None),
            size=(dp(35), dp(35)),
            pos_hint={"right": 1, "top": 1}, 
            background_normal="image/pause.png", 
            background_down="image/pause.png",
            border=(0, 0, 0, 0),
        )
        settings_button.bind(on_press=self.open_settings)
        layout.add_widget(settings_button)

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

    def open_settings(self, instance):

        settings_content = FloatLayout()

        settings_background = Image(
            source="buttons/setting-popup.png",
            size_hint=(1, 1),
            allow_stretch=True,
        )
        settings_content.add_widget(settings_background)

        sound_label = Label(
            text="Background Sound",
            font_size=dp(18),
            font_name="fonts/SplashBakery.otf",
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(dp(200), dp(50)),
            pos=(dp(50), dp(120)),
        )
        settings_content.add_widget(sound_label)

        sound_switch = Switch(
            active=self.background_sound_active,
            size_hint=(None, None),
            size=(dp(50), dp(30)),
            pos=(dp(220), dp(125)),
        )
        sound_switch.bind(active=self.toggle_background_sound)
        settings_content.add_widget(sound_switch)

        close_button = Button(
            size_hint=(None, None),
            size=(dp(60), dp(40)),
            pos_hint={"center_x": 0.5, "y": 0.05}, 
            background_normal="buttons/btn_ok.png",
            background_down="buttons/btn_ok.png",
            border=(0, 0, 0, 0),
        )
        close_button.bind(on_press=self.close_settings_popup)
        settings_content.add_widget(close_button)

        self.settings_popup = Popup(
            title="",
            content=settings_content,
            size_hint=(None, None),
            size=(dp(300), dp(200)),
            auto_dismiss=False,
            background="",
            border=(0, 0, 0, 0), title_size=0,
            separator_color=(0, 0, 0, 0),
        )
        self.settings_popup.open()

    def close_settings_popup(self, instance):
        self.settings_popup.dismiss()

    def toggle_background_sound(self, instance, value):
        app = App.get_running_app() 
        self.background_sound_active = value 

        if app.background_music:
            if value:  
                app.background_music.play()
                print("Background sound enabled")
            else:  
                app.background_music.stop()
                print("Background sound disabled")

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("paint.kv")
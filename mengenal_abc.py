from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
import string
from kivy.core.window import Window
from kivy.metrics import dp


class Game1Screen(Screen):
    popup_content = FloatLayout()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = None

        layout = FloatLayout()
        grid_container = BoxLayout(size_hint=(0.8, 0.7), pos_hint={"center_x": 0.53, "center_y": 0.49})

        WindowWidth = Window.width
        cols = 7
        if WindowWidth < 600:
            cols = 5

        grid = GridLayout(cols=cols, spacing=dp(6), padding=dp(10), size_hint=(1, 1))
        button_size = dp(60)

        self.score = 0
        self.buttons_clicked = 0
        self.total_buttons = 26 

        for index, letter in enumerate(string.ascii_uppercase, start=1):
            image_path = f"image/huruf/btn/{letter}.png"
            sound_path = f"image/voice_ alfabet/{index}.mp3"
            image_button = ImageButton(
                source=image_path, sound_path=sound_path, size_hint=(None, None), size=(button_size, button_size)
            )
            image_button.index = index
            image_button.bind(on_press=self.button_pressed)
            grid.add_widget(image_button)

        grid_container.add_widget(grid)
        layout.add_widget(grid_container)
        self.add_widget(layout)

    def play_sound(self, instance):
        if self.sound:
            self.sound.play()

    def button_pressed(self, instance):

        if not instance.clicked:
            instance.clicked = True
            self.score += 1
            self.buttons_clicked += 1

            if instance.sound_path:
                print(f"Attempting to load sound: {instance.sound_path}")
                sound = SoundLoader.load(instance.sound_path)
                if sound:
                    sound.play()
                    print(f"Playing sound: {instance.sound_path}")
                else:
                    print(f"Sound file could not be loaded: {instance.sound_path}")

        if self.buttons_clicked == self.total_buttons:
            self.show_score_popup()

    def show_score_popup(self):
        score_label = Label(
            text=f"Your Score: {self.score}",
            font_size=dp(24),
            font_name="fonts/SplashBakery.otf",
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(dp(200), dp(50)),
            pos_hint={"x": 0.7, "y": 0.25},
            )
        score_label.bind(size=score_label.setter("text_size"))

        close_button = Button(
            size_hint=(None, None),
            size=(dp(60), dp(30)),
            pos_hint={"center_x": 0.5, "y": 0.05},
            background_normal="buttons/btn_ok.png",
            background_down="buttons/btn_ok.png",
            border=(0, 0, 0, 0)
        )
        close_button.bind(on_press=self.close_popup)

        popup_content = BoxLayout(orientation='horizontal')
        popup_content.add_widget(score_label)
        popup_content.add_widget(close_button)

        self.popup = Popup(title="",
                           content=popup_content,
                           size_hint=(None, None),
                           size=(dp(305), dp(307)),
                           auto_dismiss=True,
                           background="buttons/popup_complete.png",
                           border=(0, 0, 0, 0), title_size=0,
                           separator_color=(0, 0, 0, 0),)
                           
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss() 

    def reset_game(self):
        self.score = 0
        self.buttons_clicked = 0
        for button in self.children[0].children[0].children[0].children: 
            button.clicked = False

    def go_back(self, instance=None):
        self.manager.current = "game"
        self.play_sound("music/pop-button.mp3")


class ImageButton(Button):
    source = StringProperty("")
    sound_path = StringProperty("")
    clicked = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = self.source
        self.background_down = self.source
        self.background_color = (1, 1, 1, 1)
        self.text = ""
        self.border = (0, 0, 0, 0)

    def on_press(self):
        self.background_normal = self.source
        self.clicked = True 

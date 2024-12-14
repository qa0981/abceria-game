from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Rectangle


class ClickableImage(ButtonBehavior, Image):
    pass


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            self.bg_image = Rectangle(
                source="image/bg.png",
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self.update_bg, pos=self.update_bg)

        layout = FloatLayout()

        self.title_image = Image(
            source="image/logo1.png",
            allow_stretch=True,
            size_hint=(None, None),
            size=(850, 350),
            pos_hint={"center_x": 0.5, "top": 0.9}
        )
        layout.add_widget(self.title_image)

        button_layout = GridLayout(
            cols=3,
            rows=2,
            spacing=30,
            size_hint=(None, None),
            width=800, 
            height=600,
            pos_hint={"center_x": 0.5, "center_y": 0.4}
        )

        self.button1 = ClickableImage(
            source="image/menu1.png",
            allow_stretch=True,
            size_hint=(None, None),
            size=(250, 150)
        )
        self.button1.bind(on_press=self.on_button1_click)

        self.button2 = ClickableImage(
            source="image/menu1.png",
            allow_stretch=True,
            size_hint=(None, None),
            size=(250, 150)
        )
        self.button2.bind(on_press=self.on_button2_click)

        self.button3 = ClickableImage(
            source="image/menu1.png",
            allow_stretch=True,
            size_hint=(None, None),
            size=(250, 150)
        )
        self.button3.bind(on_press=self.on_button3_click)

        self.button4 = ClickableImage(
            source="image/menu1.png",
            allow_stretch=True,
            size_hint=(None, None),
            size=(250, 150)
        )
        self.button4.bind(on_press=self.on_button4_click)

        self.button5 = ClickableImage(
            source="image/menu1.png",
            allow_stretch=True,
            size_hint=(None, None),
            size=(250, 150)
        )
        self.button5.bind(on_press=self.on_button5_click)

        button_layout.add_widget(self.button1)
        button_layout.add_widget(self.button2)
        button_layout.add_widget(self.button3)
        button_layout.add_widget(self.button4)
        button_layout.add_widget(self.button5)

        layout.add_widget(button_layout)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg_image.size = self.size
        self.bg_image.pos = self.pos

    def on_button1_click(self, instance):
        print("Game 1 clicked!")
        self.start_game1()

    def on_button2_click(self, instance):
        print("Game 2 clicked!")
        self.start_game2()

    def on_button3_click(self, instance):
        print("Game 3 clicked!")
        self.start_game3()

    def on_button4_click(self, instance):
        print("Game 4 clicked!")
        self.start_game4()

    def on_button5_click(self, instance):
        print("Game 5 clicked!")
        self.start_game5()

    def start_game1(self):
        self.manager.current = "game1"

    def start_game2(self):
        self.manager.current = "game2"

    def start_game3(self):
        self.manager.current = "game3"

    def start_game4(self):
        self.manager.current = "game4"

    def start_game5(self):
        self.manager.current = "game5"